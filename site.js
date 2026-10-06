/* ===== Little Gasp – shared header, footer and phone menu =====
   Edit links here once; every page picks them up.
   Page options on <body>: data-header="static" (header doesn't stick), data-footer="none". */
(function(){
  const IG = "https://instagram.com/littlegasp.co/";
  const EMAIL = "littlegasp.orders@gmail.com";
  const body = document.body;

  const blobs = document.createElement("div");
  blobs.className = "blobs"; blobs.setAttribute("aria-hidden", "true");
  blobs.innerHTML = "<i></i><i></i><i></i>";

  const ICON_OPEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  const ICON_CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';

  const bar = document.createElement("header");
  bar.className = "bar glass" + (body.dataset.header === "static" ? " static" : "");
  bar.innerHTML =
    '<a class="logo" href="/"><img src="/apple-touch-icon.png" alt=""><span>Little Gasp</span></a>' +
    '<nav id="nav">' +
      '<a href="/#designs">Designs</a>' +
      '<a href="/#how">How it works</a>' +
      '<a href="' + IG + '" target="_blank" rel="noopener">Instagram</a>' +
      '<a class="cta-s" href="/#designs">Create a surprise</a>' +
    '</nav>' +
    '<button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav">' + ICON_OPEN + '</button>';
  body.prepend(blobs, bar);

  const btn = bar.querySelector(".menu-btn");
  function setMenu(open){
    bar.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open);
    btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    btn.innerHTML = open ? ICON_CLOSE : ICON_OPEN;
  }
  btn.addEventListener("click", e => { e.stopPropagation(); setMenu(!bar.classList.contains("open")); });
  bar.querySelectorAll("nav a").forEach(a => a.addEventListener("click", () => setMenu(false)));
  document.addEventListener("click", e => { if (!bar.contains(e.target)) setMenu(false); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") setMenu(false); });

  if (body.dataset.footer !== "none"){
    document.addEventListener("DOMContentLoaded", () => {
      const f = document.createElement("footer");
      f.className = "site";
      f.innerHTML =
        '<nav><a href="/terms.html">Terms</a><a href="/refund.html">Refunds</a><a href="/privacy.html">Privacy</a><a href="/contact.html">Contact</a><a href="' + IG + '" target="_blank" rel="noopener">Instagram</a></nav>' +
        '<p>Little Gasp, operated by Aniket Nandkumar Gurav, Mumbai, India · <a href="mailto:' + EMAIL + '">' + EMAIL + '</a></p>';
      body.appendChild(f);
    });
  }
})();
