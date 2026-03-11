# Authentication

!!! success "Current MVP"
    API key-based authentication is available from Phase 3. OAuth2 with JWT and RBAC are added in Phase 4.

---

## Authentication Methods

### API Key (Developer API)

Include your API key in every request via the `X-API-Key` header:

```bash
curl -H "X-API-Key: YOUR_API_KEY" \
     https://api.finsight.dev/v1/companies
```

### JWT (Dashboard / Session)

!!! info "Planned Architecture (Future Phases)"
    JWT-based session auth for the web dashboard is implemented in Phase 4.

<!-- Describe OAuth2 password flow, JWT claims structure, HttpOnly cookie handling -->

---

## Obtaining an API Key

<!-- Describe sign-up flow, key generation on dashboard, key rotation procedure -->

---

## Role-Based Access Control (RBAC)

!!! info "Planned Architecture (Future Phases)"
    RBAC with Keycloak or Auth0 is implemented in Phase 4.

| Role | Access Level |
|---|---|
| `anonymous` | Public landing page only |
| `free` | Basic company metrics, limited API |
| `paid` | Full dashboard, deep analytics, full API |
| `admin` | All resources + user management |

---

## Token Expiry and Refresh

<!-- Describe access token TTL (15 min), refresh token TTL (30 days), silent refresh flow -->

---

## Security Best Practices

<!-- Describe key storage guidance for developers: environment variables, never in client code -->
