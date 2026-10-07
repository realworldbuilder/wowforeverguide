# Fonts

## LifeCraft
- Author: Eliot Truelove
- Source: https://www.dafont.com/lifecraft.font (file in the download: `LifeCraft_Font.ttf`, 2008)
- Licence: donationware. The author asks for a donation (PayPal, Cash App or Venmo links on the dafont page) and sets no stated restriction on web or commercial use.
- Files: `LifeCraft.ttf` is the original, renamed. `LifeCraft.woff2` was converted from it with fontTools, no glyph changes.
- Used as `--title` in `site/assets/site.css`: h1, h2, the brand mark and the hero stat numbers. One weight, no italic, so those rules set weight 400 and `font-synthesis: none`.
- Covers ASCII, curly quotes, bullets and the Euro sign. No accented letters and no en or em dash, so those characters fall back to Chakra Petch.
