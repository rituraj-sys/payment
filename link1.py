import hashlib
import uuid

# PayU parameters
merchant_key = 'kPFnBJ'
salt = 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxQyxletw5kE/0R+8uNEHOobYHYygYpp27YLnf9WAc4sz1+nMMwh9+y4OyTvqvUQh+I7+Lk85XoVVAUDLLu0IsyvJ1hCEQjJH7WkUqk4XZF+r8/X4Fxzr0Wf4CfLZbLn7PO6lOjhGK4bPoViFuQJ8BVtGEhFp6ed169jRGMmTOj44Mno9eFbbzwpB0Rh40SLUuIjf8HGHTX8cJ1vipFNEP7ASH56kHxdOZXDZ35WSjZx2j7VQua5rmCCwRL/XYAkLpzVWLVFTixpUt7U+IBSJ7saTEKfITConb3s6BugNdB4Vnos380hiOi9bS5FIkjrM/GJ5t5+2APJoZyuoaBLJnAgMBAAECggEAe6oqWe25n+se7IQWx/wrANXuYP77JR9wIR4c7rKHx/8uEFkWVItFX7bpfMb+urpkm2OjKOQH6zihegm5NkrAovE+718rlhkLaviSEl7y3P6DsNXESpGwfnId9Gw+6CPq0faEakpQ0LwfP/J+xiUNCOkhqDqRyKomKreCxoo3q6ZvRODXddTQM2u9s8C/1RGM5Utmhu8aJyj88LJS96wiULo/IVR0EaGV6TxGFJHJcJHakN0LaaJtwvW2X0i2H4lpXMfSvr2cRUpsMEG+iuAM/HxAn75LAY25tEn+Pj4M4tWf1iIC3PlN2jKwu2hpo6ZzM5ddlsdgfkgHY76aa9TCoQKBgQDglNkCh+ssMWwV4etGH9yiQKalw7FVirhJkrRg3Lftl8tgk8sOR2aRIZG+2n6IBdbsrP9LDgsAAIs9vICWMNbcKUCVFKo0K1JJC70dLutE+qOrPYH24KWqsc+I9G44MRB8mSqT9v9U2hDbn6/ZN4Hg8e6zRpDxaewcf3aChFZpcQKBgQDKD6SlwTfXA1VY2caDUgiLDDWWioPvk0penwtqDCR7hXNNSUh9FidIGJqU0MCqvGsuENbjGUGPnhWrSUjfcQ/K2mlPycKNJS7e2cCIjK1mFPSdjF+XQ3qHJSgOZ4FtbOPjFhKhLS3Ru9WtV8iZLUiJnNer1l1a5PRp/A7Lcv4tVwKBgDn89RO8OLMOh9QWo4NV0shqXR1MLEvkJ7WHld+03iERIshrIPEs6oTq4BEhpa5Fo7s06C5fD+QOP+XO+HzPW4s5c52K2m/iB7sotsoERWdoOD6NATPXya8LfoTkaFlGAfXKLr5J9p/YNqYe028I8BY/Id1UiTRsnzS0jMsilJVhAoGAHqS+sJCb+lS8Fcx5KaNAPm4sllcNaUDqL21pWrzar4zujpMFlkrMzEdG8jiyb3JBwuu02x4SbkhoOuDTV2ebIIV9ISeVBLjV4eAeLdc/2NJmwpnuSU9nfqVo7L5Px5uS9/Z5/s2OPFeDMVW1y10tugj6QEozQDymwIgEamBXIeMCgYEA34BcE+rd6UHL5te29KAT4A2uanfDxcmJXkHmcleAQ1HOf/Fu5wCLJ7WM8KvoxIN/St2QM45D55vH2i8MwHlcMvEoeBHWxD//0VJN1KSYAg9IHI3zlIEdXIFhPVG5t+ozzO2emlsl1MjPXkF3uDnOnW70VkAuIMYCjjYx09XfsSA='
base_url = 'https://secure.payu.in/_payment'  # Use the appropriate endpoint URL

# Payment details
amount = '1.00'  # Amount to be paid
product_info = 'Test Product'
firstname = 'John'
email = 'john.doe@example.com'
phone = '9999999999'
surl = 'http://127.0.0.1:5000/succ'  # Success URL
furl = 'http://127.0.0.1:5000/fail'  # Failure URL

# Generate transaction ID
txnid = str(uuid.uuid4())  # Should be unique for each transaction

# Prepare hash string
hash_string = f"{merchant_key}|{txnid}|{amount}|{product_info}|{firstname}|{email}|||||||||||{salt}"
hash_object = hashlib.sha512(hash_string.encode('utf-8'))
hashh = hash_object.hexdigest()

# Generate HTML form
html_form = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting to PayU</title>
</head>
<body onload="document.forms['payu_form'].submit()">
    <h1>Redirecting to PayU...</h1>
    <form action="{base_url}" method="post" name="payu_form">
        <input type="hidden" name="key" value="{merchant_key}">
        <input type="hidden" name="txnid" value="{txnid}">
        <input type="hidden" name="amount" value="{amount}">
        <input type="hidden" name="productinfo" value="{product_info}">
        <input type="hidden" name="firstname" value="{firstname}">
        <input type="hidden" name="email" value="{email}">
        <input type="hidden" name="phone" value="{phone}">
        <input type="hidden" name="surl" value="{surl}">
        <input type="hidden" name="furl" value="{furl}">
        <input type="hidden" name="hash" value="{hashh}">
        <input type="hidden" name="service_provider" value="payu_paisa">
    </form>
</body>
</html>
"""

# Save the HTML form to a file
with open("payu_redirect.html", "w") as file:
    file.write(html_form)
print(html_form)

print("HTML form generated and saved as payu_redirect.html. Open this file in a web browser to proceed with the payment.")
