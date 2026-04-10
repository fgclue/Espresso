# Expresso 1

## DB

token -> jwt with id that is stored in db
item -> name, code, price (optional)
user -> id, email, name, password, role, fiscal barcode (optional)
transaction -> id, operator, epoch, items, paid
roles -> name, permissions

## Endpoints

- ![POST](/readme/POST.svg) /user/token <- id or email, password -> jwt token

---

- ![GET](/readme/GET.svg) /item/get <- barcode -> name, code, price
- ![PUT](/readme/PUT.svg) /item/new <- barcode, name, code, price -> status
- ![PATCH](/readme/PATCH.svg) /item/edit <- optional: (barcode, name, code, price) -> status

---

- ![PATCH](/readme/PATCH.svg) /user/name <- new_name -> status
- ![PATCH](/readme/PATCH.svg) /user/email <- password, new_email -> status
- ![PATCH](/readme/PATCH.svg) /user/password <- old_password, new_password -> status

---

- ![PUT](/readme/PUT.svg) /transactions/new <- items -> id, epoch(operator derived from token)
- ![PATCH](/readme/PATCH.svg) /transactions/finish <- transaction id -> status (operator that is allowed to edit derived from token)
- ![GET](/readme/GET.svg) /transactions/analytics <- start, end, filter -> data
- ![GET](/readme/GET.svg) /transactions/analytics <- start, end, filter -> data

---

- ![GET](/readme/GET.svg) /fiscal/test <- fiscal key -> result
- ![PATCH](/readme/PATCH.svg) /fiscal/set <- new_key -> status