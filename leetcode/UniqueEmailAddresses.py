# url: https://leetcode.com/problems/unique-email-addresses/description/
from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    unique_emails = set()
    for email in emails:
        name, domain = email.split("@")
        name = name.replace(".", "").split("+")[0]
        unique_emails.add(name + "@" + domain)

    return len(unique_emails)


print(
    numUniqueEmails(["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"])
)
