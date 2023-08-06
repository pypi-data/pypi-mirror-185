# OnePassword CLI v2 python wrapper

Quick n dirty python wrapper for the [1password cli](https://developer.1password.com/docs/cli) **version 2**.

## Setup

- Install the `op` cli by following [these instructions](https://developer.1password.com/docs/cli/get-started#install). 
- Make sure you have `op` in your PATH and that it is __not version 1__
```
$ op --version
2.12.0
```
- Have your 1password username, password, and signin url handy
- `pip install onepassword2` \
   -- or, for a local install -- \
   `make local install`

## Usage

### CLI

The `op` cli tool has a _lot_ of options for managing multiple accounts, profiles, etc.  Sessions opened with the cli terminate after 10 minutes, requirinng the user to re-authenticate interactively.  This is good security.  However, if you need long running, non-interactive usage, this is a hindrance. This python module comes with a handy CLI to automagify the signin process.

```bash
export OP_ACCOUNT='user@example.com'
export OP_PASSWORD="your password"
export OP_HOSTNAME="yourhost.1password.com"

eval $(op-signin)

...

$ op vault list

ID                            NAME
naaizerttzertzefzyhjroeqrq    Private


```

### In python scripts

```python

username = "user@example.com"
password = "your password"
hostname = "yourhost.1password.com"
o = OP2( username, password, hostname)
o.signin()

for v in o.vaults():
    print(v)

```