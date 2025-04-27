class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        receivers = set[str]()
        for email in emails:
            parts = email.split("@", 1)
            if len(parts) != 2:
                continue
            local, domain = parts
            local = "".join(local.split("."))
            if (idx := local.find("+")) >= 0:
                local = local[:idx]
            receivers.add(f"{local}@{domain}")
        return len(receivers)
