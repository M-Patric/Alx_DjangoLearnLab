# LibraryProject - Django Setup
# Security Notes (summary)

1. Settings
- DEBUG must be False in production.
- Cookies: CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE set to True in production.
- X_FRAME_OPTIONS = "DENY", SECURE_BROWSER_XSS_FILTER = True, SECURE_CONTENT_TYPE_NOSNIFF = True.
- CSP implemented via django-csp or SecurityHeadersMiddleware.

2. Forms & CSRF
- All HTML forms include {% csrf_token %}.
- AJAX requests must set X-CSRFToken header.

3. Data handling
- Use Django ORM and ModelForms. Avoid raw SQL.
- Use built-in validation and sanitize file uploads (size/type).

4. Files & deployment
- MEDIA files served by proper server (nginx/Cloud Storage), not Django in production.
- SECRET_KEY, DB credentials, and other secrets come from environment variables.

5. Testing
- Test CSRF, XSS, CSP, and cookie flags in dev/staging before production.

6. Notes:
- Many cookie and HSTS settings require HTTPS — enable them only after you have SSL/TLS configured.
