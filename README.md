# Sean Personal Assistant — Public Information Site

This is a **static, public informational website** for the owner-operated Sean Personal Assistant Google OAuth application. It is not the app itself and contains no account sign-in, database, Google OAuth client secret, token or tracking script.

## Files

- `index.html` — Homepage
- `privacy.html` — Privacy policy
- `terms.html` — Terms of use
- `styles.css` — Local responsive styles (no CDN)
- `.nojekyll` — GitHub Pages static file flag

## Deployment

1. Use a *separate public GitHub repository*, ideally `e93116-droid.github.io`.
2. Publish from the main branch root via **Settings → Pages → Deploy from a branch**.
3. Verify HTTPS and content before placing URLs on Google OAuth branding.
4. For Google OAuth authorized domains, verify ownership of a **dedicated domain** in Google Search Console. A `github.io` shared hosted domain alone may not satisfy Google's domain ownership verification policy.
5. Do not add real Google access/refresh tokens, Gmail data, user identifiers beyond the published contact email, credentials, or internal infrastructure details.
6. If applying for an `is-a.dev` free subdomain, follow its current contribution requirements personally. The upstream project explicitly disallows AI-generated registration PRs; do not auto-submit them.

## Google OAuth

The app name should match **Sean Personal Assistant**. Use the hosted public homepage and privacy page when Google allows the domain. Publishing from Testing can remove the testing-specific short refresh-token lifetime, but Google may still require branding verification or user warnings. **Publishing does not restore an expired refresh token**; the owner must re-authorize through Google's normal account consent flow.

## Changes

Keep the privacy policy synchronized with actual Google-data collection, AI-provider disclosure, security measures and retention behavior. Website publication does not change any local assistant, HOOYA or LION service.
