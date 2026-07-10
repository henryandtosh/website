# Henry & Tosh Limited website

A static institutional brochure site for Henry & Tosh Limited, deployed on Netlify.

## Page

- `index.html` — company overview, strategy and governance

The previous static login and dashboard were deliberately retired because static HTML cannot provide secure authentication or protect confidential data. Their old URLs redirect to the homepage through `netlify.toml`.

## Local development

```bash
python3 -m http.server 8000
```

Open <http://localhost:8000>.

## Validation

```bash
python3 -m unittest discover -s tests -v
npx --yes html-validate@10.4.0 '*.html'
node --check script.js
```

## Deployment and security

`netlify.toml` supplies:

- redirects for the retired portal URLs
- Content Security Policy
- clickjacking protection
- MIME-sniffing protection
- restrictive browser permissions
- controlled caching for image assets

## Company information

Henry & Tosh Limited is registered in England & Wales under Company No. 11919030. The site is informational only and does not constitute an offer to invest.
