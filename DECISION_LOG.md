# DevSecOps Pipeline – Decision Log

## 1. Why multiple security tools (Semgrep, Gitleaks, Trivy, ZAP)?
To ensure layered security coverage across the SDLC:
- Semgrep → Static code vulnerabilities (SAST)
- Gitleaks → Secrets detection
- Trivy → Container vulnerabilities
- OWASP ZAP → Runtime (DAST)

This ensures vulnerabilities are detected across code, dependencies, and runtime behavior.

---

## 2. Why `continue-on-error: true`?
To prevent early pipeline termination and ensure:
- All security tools execute
- Full visibility of security posture

Instead of failing fast, the pipeline collects all findings for better analysis.

---

## 3. Why limit ZAP scan time (`-m 2`)?
To optimize CI/CD performance:
- Prevent long-running scans
- Maintain fast feedback loops for developers

---

## 4. Why use Docker for all tools?
To ensure:
- Consistent execution environments
- No dependency conflicts
- Easy portability across systems

---

## 5. Why use baseline scan (not full active scan)?
- Faster execution in CI
- Suitable for early-stage applications
- Reduces risk of breaking test environments

---

## 6. Why allow vulnerabilities in project?
The application intentionally contains:
- Missing security headers
- Basic misconfigurations

Purpose:
- Demonstrate detection capabilities
- Show real-world pipeline behavior

---

## 7. Why chmod 777 used?
Used in CI to resolve container write permission issues.

Note:
In production, proper user/group mapping would be implemented instead.

---

## 8. Why GitHub Actions?
- Native CI/CD integration
- Easy setup
- Widely used in industry

---

## 9. Why security as a gate (failing pipeline)?
To enforce:
- Secure coding practices
- Prevention of vulnerable deployments

Pipeline fails when critical issues are detected.

---

## 10. Key Learning
Security is not a single step—it is integrated across:
- Code
- Build
- Deployment
- Runtime