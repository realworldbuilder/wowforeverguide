// Launch status chip, road-to-launch highlighting and search. No dependencies.
(function () {
  var root = document.documentElement.getAttribute('data-root') || '';
  var now = Date.now();
  var DAY = 86400000;
  var betaEnd = Date.UTC(2026, 9, 22, 7);    // end of October 21, Pacific time
  var launch = Date.UTC(2026, 10, 4, 23);    // November 4, 3:00 p.m. PST

  var chip = document.getElementById('status');
  if (chip) {
    var days = Math.floor((launch - now) / DAY);
    if (now < betaEnd) chip.textContent = 'Beta open to Oct 21 · launch in ' + days + (days === 1 ? ' day' : ' days');
    else if (now < launch) { chip.textContent = 'Launch Nov 4 · ' + (days < 1 ? 'today' : 'in ' + days + (days === 1 ? ' day' : ' days')); chip.className += ' wait'; }
    else chip.textContent = 'Live since Nov 4';
  }

  // Road to launch: fade what has passed and mark the next dated event.
  var marked = false;
  document.querySelectorAll('.road li[data-start]').forEach(function (li) {
    var start = li.getAttribute('data-start');
    if (!start) return;
    var t = Date.parse(start + 'T23:59:59-08:00');
    if (t < now) li.classList.add('done');
    else if (!marked) { li.classList.add('next'); marked = true; }
  });

  // Search
  var input = document.getElementById('q');
  var list = document.getElementById('hits');
  if (!input || !list) return;
  var index = null;
  function load() {
    if (index) return Promise.resolve(index);
    return fetch(root + 'search.json').then(function (r) { return r.json(); }).then(function (d) { index = d; return d; });
  }
  function show(items, q) {
    list.innerHTML = '';
    if (!q) { list.hidden = true; return; }
    if (!items.length) {
      var li = document.createElement('li'); li.className = 'none'; li.textContent = 'Nothing found for "' + q + '"'; list.appendChild(li);
    }
    items.slice(0, 8).forEach(function (it) {
      var li = document.createElement('li'), a = document.createElement('a'), s = document.createElement('small');
      a.href = root + it.u; a.textContent = it.t; s.textContent = it.k; a.appendChild(s); li.appendChild(a); list.appendChild(li);
    });
    list.hidden = false;
  }
  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase();
    if (!q) return show([], '');
    load().then(function (d) {
      var words = q.split(/\s+/);
      show(d.filter(function (it) {
        var hay = (it.t + ' ' + it.k + ' ' + it.x).toLowerCase();
        return words.every(function (w) { return hay.indexOf(w) !== -1; });
      }), q);
    });
  });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { input.value = ''; show([], ''); }
    if (e.key === 'Enter') { var a = list.querySelector('a'); if (a) location.href = a.href; }
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.search')) list.hidden = true; });
})();
