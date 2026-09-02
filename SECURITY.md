# Security Policy

## 🔒 Security Best Practices

### API Key Management

✅ **DO:**
- Use environment variables via `.env` file
- Keep `.env` out of version control (use `.gitignore`)
- Enable IP whitelisting on exchange APIs
- Use separate API keys for different bots
- Rotate API keys periodically
- Use read-only or trade-only permissions
- Store backups of API keys securely

❌ **DON'T:**
- Hardcode API keys in code
- Commit `.env` file to git
- Share API keys via email or chat
- Use the same API key for multiple apps
- Enable unnecessary API permissions
- Use master account keys

### Email Security

✅ **DO:**
- Use Gmail App Passwords, not main password
- Enable 2-Step Verification
- Use SMTP with TLS/SSL
- Store email password in `.env`
- Use a dedicated email for alerts

❌ **DON'T:**
- Use your main Gmail password
- Send email passwords in plain text
- Use outdated SMTP connections

### Running the Bot

✅ **DO:**
- Run on a secure, updated server
- Keep Python and dependencies updated
- Monitor logs regularly
- Use firewall rules
- Enable server firewall
- Back up important data
- Use VPN if accessing remotely
- Set resource limits

❌ **DON'T:**
- Run as root user
- Disable firewall
- Expose bot to the internet
- Ignore security warnings
- Skip dependency updates

### Code Security

- All dependencies are from PyPI
- No external scripts downloaded at runtime
- No telemetry or data collection
- Open source for community review
- Regular dependency updates recommended

## 🛡️ Vulnerability Disclosure

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. Email: mr.muhammad.saad.siddiqui@gmail.com
3. Include:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

4. Allow time for response and patch
5. Coordinate responsible disclosure

## 📋 Security Checklist

Before using the bot in production:

- [ ] `.env` file is in `.gitignore`
- [ ] API keys use IP whitelisting
- [ ] API permissions are minimal (trading only)
- [ ] Email uses App Password
- [ ] 2-Step Verification enabled
- [ ] Server is updated (apt update && apt upgrade)
- [ ] Firewall is configured
- [ ] Regular backups configured
- [ ] Monitoring/logging configured
- [ ] Tested on small amounts first

## 🚨 If Compromised

1. **Immediately revoke** all API keys from exchange settings
2. **Stop** the bot
3. **Rotate** email password
4. **Monitor** exchange accounts for unauthorized activity
5. **Change** server password
6. **Review** logs for suspicious activity
7. **Generate** new API keys
8. **Update** `.env` with new keys
9. **Resume** operations

## 📚 Resources

- [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/)
- [Python Security](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Exchange API Security](https://www.binance.com/en/support/articles/12520952406)
- [Gmail App Passwords](https://support.google.com/accounts/answer/185833)

## 🔄 Updates

Keep your installation secure:

```bash
# Update Python dependencies
pip install --upgrade -r requirements.txt

# Check for vulnerabilities
pip install safety
safety check

# Pull latest code
git pull origin main
```

---

**Remember: You are responsible for securing your own API keys and funds.**
