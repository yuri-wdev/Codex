// ─── STATE ───────────────────────────────────────────────
        let books = [
            { id: 1, titulo: 'Dom Quixote', autor: 'Cervantes', ano: 1605, genero: 'Aventura', emprestado: false },
            { id: 2, titulo: 'Grande Sertão: Veredas', autor: 'Guimarães Rosa', ano: 1956, genero: 'Romance', emprestado: true, tomador: 'João Silva', devolucao: '2026-03-20' },
            { id: 3, titulo: 'O Alquimista', autor: 'Paulo Coelho', ano: 1988, genero: 'Ficção', emprestado: false },
        ];
        let nextId = 4, selectedBook = null;

        // ─── TABS ────────────────────────────────────────────────
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
                tab.classList.add('active');
                document.getElementById('tab-' + tab.dataset.tab).classList.add('active');
            });
        });

        // ─── TOAST ───────────────────────────────────────────────
        function showToast(msg) {
            const t = document.getElementById('toast');
            t.textContent = msg; t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 2500);
        }

        // ─── MODALS ──────────────────────────────────────────────
        function openModal(id) { document.getElementById(id).classList.add('open'); }
        function closeModal(id) { document.getElementById(id).classList.remove('open'); }

        document.querySelectorAll('[data-close]').forEach(btn =>
            btn.addEventListener('click', () => closeModal(btn.dataset.close))
        );
        document.querySelectorAll('.modal-overlay').forEach(overlay =>
            overlay.addEventListener('click', e => { if (e.target === overlay) overlay.classList.remove('open'); })
        );

        // ─── HELPERS ─────────────────────────────────────────────
        function createBookItem(book, onClick, subtitle) {
            const item = document.createElement('div');
            item.className = 'book-item';
            item.innerHTML = `
        <span><strong>${book.titulo}</strong> — ${book.autor}${subtitle ? ' <span style="color:#6b7280;font-weight:400">· ' + subtitle + '</span>' : ''}</span>
        <span class="book-item-year">${book.ano}</span>`;
            item.addEventListener('click', onClick);
            return item;
        }

        // ─── ADICIONAR ───────────────────────────────────────────
        document.getElementById('btn-adicionar').addEventListener('click', () => {
            ['add-titulo', 'add-autor', 'add-ano', 'add-genero'].forEach(id => document.getElementById(id).value = '');
            openModal('modal-adicionar');
        });
        document.getElementById('confirm-adicionar').addEventListener('click', () => {
            const titulo = document.getElementById('add-titulo').value.trim();
            if (!titulo) { document.getElementById('add-titulo').focus(); return; }
            const autor = document.getElementById('add-autor').value.trim();
            const ano = document.getElementById('add-ano').value.trim();
            const genero = document.getElementById('add-genero').value.trim();
            books.push({ id: nextId++, titulo, autor, ano, genero, emprestado: false });
            closeModal('modal-adicionar');
            showToast('📚 Livro "' + titulo + '" adicionado!');
        });

        // ─── EDITAR ──────────────────────────────────────────────
        document.getElementById('btn-editar').addEventListener('click', () => {
            const list = document.getElementById('list-editar');
            list.innerHTML = '';
            if (!books.length) { list.innerHTML = '<p style="color:#9ca3af;font-size:14px">Nenhum livro no acervo.</p>'; }
            else books.forEach(b => list.appendChild(createBookItem(b, () => {
                selectedBook = b;
                closeModal('modal-editar-lista');
                document.getElementById('edit-titulo').value = b.titulo;
                document.getElementById('edit-autor').value = b.autor;
                document.getElementById('edit-ano').value = b.ano;
                document.getElementById('edit-genero').value = b.genero;
                openModal('modal-editar-form');
            })));
            openModal('modal-editar-lista');
        });
        document.getElementById('confirm-editar').addEventListener('click', () => {
            if (!selectedBook) return;
            selectedBook.titulo = document.getElementById('edit-titulo').value.trim() || selectedBook.titulo;
            selectedBook.autor = document.getElementById('edit-autor').value.trim() || selectedBook.autor;
            selectedBook.ano = document.getElementById('edit-ano').value.trim() || selectedBook.ano;
            selectedBook.genero = document.getElementById('edit-genero').value.trim() || selectedBook.genero;
            closeModal('modal-editar-form');
            showToast('✏️ Livro atualizado com sucesso!');
            selectedBook = null;
        });

        // ─── REMOVER ─────────────────────────────────────────────
        document.getElementById('btn-remover').addEventListener('click', () => {
            selectedBook = null;
            const list = document.getElementById('list-remover');
            list.innerHTML = '';
            if (!books.length) { list.innerHTML = '<p style="color:#9ca3af;font-size:14px">Nenhum livro no acervo.</p>'; }
            else books.forEach(b => {
                const item = createBookItem(b, () => {
                    document.querySelectorAll('#list-remover .book-item').forEach(i => i.classList.remove('selected'));
                    item.classList.add('selected'); selectedBook = b;
                });
                list.appendChild(item);
            });
            openModal('modal-remover');
        });
        document.getElementById('confirm-remover').addEventListener('click', () => {
            if (!selectedBook) return;
            const nome = selectedBook.titulo;
            books = books.filter(b => b.id !== selectedBook.id);
            closeModal('modal-remover');
            showToast('🗑️ Livro "' + nome + '" removido!');
            selectedBook = null;
        });

        // ─── NOVO EMPRÉSTIMO ──────────────────────────────────────
        document.getElementById('btn-novo-emprestimo').addEventListener('click', () => {
            const select = document.getElementById('emp-livro');
            const disponiveis = books.filter(b => !b.emprestado);
            select.innerHTML = '';
            if (!disponiveis.length) { select.innerHTML = '<option disabled>Nenhum livro disponível</option>'; }
            else disponiveis.forEach(b => {
                const opt = document.createElement('option');
                opt.value = b.id; opt.textContent = b.titulo + ' — ' + b.autor;
                select.appendChild(opt);
            });
            document.getElementById('emp-tomador').value = '';
            document.getElementById('emp-devolucao').value = '';
            openModal('modal-novo-emprestimo');
        });
        document.getElementById('confirm-emprestimo').addEventListener('click', () => {
            const livroId = parseInt(document.getElementById('emp-livro').value);
            const tomador = document.getElementById('emp-tomador').value.trim();
            const devolucao = document.getElementById('emp-devolucao').value;
            if (!tomador) { document.getElementById('emp-tomador').focus(); return; }
            const book = books.find(b => b.id === livroId);
            if (book) { book.emprestado = true; book.tomador = tomador; book.devolucao = devolucao; }
            closeModal('modal-novo-emprestimo');
            showToast('📖 Empréstimo de "' + book.titulo + '" registrado!');
        });

        // ─── DEVOLUÇÃO ────────────────────────────────────────────
        document.getElementById('btn-devolucao').addEventListener('click', () => {
            selectedBook = null;
            const list = document.getElementById('list-devolucao');
            list.innerHTML = '';
            const emprestados = books.filter(b => b.emprestado);
            if (!emprestados.length) { list.innerHTML = '<p style="color:#9ca3af;font-size:14px">Nenhum livro emprestado no momento.</p>'; }
            else emprestados.forEach(b => {
                const item = createBookItem(b, () => {
                    document.querySelectorAll('#list-devolucao .book-item').forEach(i => i.classList.remove('selected'));
                    item.classList.add('selected'); selectedBook = b;
                }, b.tomador);
                list.appendChild(item);
            });
            openModal('modal-devolucao');
        });
        document.getElementById('confirm-devolucao').addEventListener('click', () => {
            if (!selectedBook) return;
            const nome = selectedBook.titulo;
            selectedBook.emprestado = false; selectedBook.tomador = null; selectedBook.devolucao = null;
            closeModal('modal-devolucao');
            showToast('✅ "' + nome + '" devolvido com sucesso!');
            selectedBook = null;
        });