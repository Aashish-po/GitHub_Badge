# Security Policy

## Supported Versions

We support security updates for the following versions:

| Version | Supported | Status |
|---------|-----------|--------|
| 2.x     | ✅ Yes    | Active Development |
| 1.x     | ⚠️ Partial | Limited Support |
| 0.x     | ❌ No     | Deprecated |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please **do not** open a public GitHub issue. Instead, follow these steps:

### How to Report

1. **Visit GitHub Security Advisory:**
   - Go to [GitHub Security Advisory](https://github.com/Aashish-po/GitHub__Badge/security/advisories)
   - Click "Report a vulnerability"

2. **Provide Details:**
   - Description of the vulnerability
   - Impact and severity
   - Steps to reproduce
   - Suggested fix (if available)

3. **Wait for Response:**
   - Maintainers will acknowledge receipt within 48 hours
   - We'll work on a fix and timeline
   - Embargo period before public disclosure

### What to Include

```
**Vulnerability Title:** [Clear, descriptive title]

**Description:** [Detailed description of the issue]

**Severity:** [Critical/High/Medium/Low]

**Impact:** [How could this be exploited?]

**Steps to Reproduce:**
1. [First step]
2. [Second step]
3. [...]

**Suggested Fix:** [Optional - your fix or recommendation]

**Your Information:**
- Name/Handle: [Your GitHub handle]
- Email: [Contact email]
```

## Security Best Practices

### For Users

When using this project:

✅ **DO:**
- Keep your GitHub account secure
- Use responsible disclosure practices
- Report vulnerabilities privately
- Review code before running scripts
- Keep dependencies updated

❌ **DON'T:**
- Share access tokens publicly
- Test on unauthorized systems
- Exploit vulnerabilities maliciously
- Disclose vulnerabilities publicly before fix

### For Contributors

When contributing:

✅ **DO:**
- Review security implications of changes
- Follow secure coding practices
- Sanitize user input
- Use environment variables for secrets
- Add security tests where applicable

❌ **DON'T:**
- Commit credentials or tokens
- Use hardcoded secrets
- Ignore security warnings
- Skip validation/sanitization

## Compliance

This project aims to comply with:

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## Disclosure Timeline

### Responsible Disclosure Process

1. **Report Received** (Day 0)
   - Initial acknowledgment within 48 hours
   - Severity assessment
   - Create private advisory

2. **Investigation** (Days 1-14)
   - Validate the vulnerability
   - Determine scope and impact
   - Work on fix

3. **Fix Development** (Days 1-30)
   - Create patch
   - Test thoroughly
   - Prepare advisory

4. **Review & Testing** (Before release)
   - Security review
   - Community testing (if applicable)
   - Final validation

5. **Release** (When ready)
   - Release patched version
   - Publish advisory
   - Credit reporter

6. **Follow-up**
   - Monitor for issues
   - Provide support
   - Implement monitoring

## Security Contact

**Primary Contact:**
- GitHub Issues: [Report a vulnerability](https://github.com/Aashish-po/GitHub__Badge/security/advisories)

**Alternative:**
- Create private security advisory
- Tag with `security` label

## Acknowledgments

We appreciate the security researchers and community members who responsibly disclose vulnerabilities. Thank you for helping keep this project secure! 🔒

## Related Resources

- [GitHub Security Advisories](https://github.com/advisories)
- [OWASP Security Guidelines](https://owasp.org/)
- [CWE - Common Weakness Enumeration](https://cwe.mitre.org/)
- [GitHub Security Docs](https://docs.github.com/en/code-security)
