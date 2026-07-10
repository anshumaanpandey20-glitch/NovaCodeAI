document.addEventListener('DOMContentLoaded', function () {

	// Toggle code view
	document.querySelectorAll('.view-btn').forEach(function (btn) {
		btn.addEventListener('click', function (e) {
			e.preventDefault();
			var id = btn.getAttribute('data-id');
			var el = document.getElementById('code-' + id);
			if (!el) return;
			if (el.style.display === 'none' || el.style.display === '') {
				el.style.display = 'block';
				btn.textContent = 'Hide';
			} else {
				el.style.display = 'none';
				btn.textContent = 'View';
			}
		});
	});

	// Copy code
	document.querySelectorAll('.copy-btn').forEach(function (btn) {
		btn.addEventListener('click', function () {
			var id = btn.getAttribute('data-id');
			var el = document.querySelector('#code-' + id + ' pre');
			if (!el) return;
			var text = el.innerText;
			navigator.clipboard && navigator.clipboard.writeText(text).then(function () {
				btn.textContent = 'Copied';
				setTimeout(function () { btn.textContent = 'Copy'; }, 1500);
			});
		});
	});

});
