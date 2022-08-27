<p align="center">
    <h1 align = "center">Command-line Subnetting Calculator - Created in Python!</h1>
</p>
<p align="center">
    Scalc is a simple command-line subnet calculator. It can be used to generate markdown tables of subnet information.
</p>
 
---

## Usage
1. Navigate into the project directory:
    ```bash
    cd subnet-calculator
    ```
2. Install the module:
    ```bash
    pip install .
    ```
3. Run the command-line tool:
    ```bash
    ❯ scalc --help

    Usage: scalc [OPTIONS] IP_ADDRESS

    ╭─ Arguments ────────────────────────────────────────────────────────────────────────╮
    │ *    ip_address      TEXT  IP address. [default: None] [required]                  │
    ╰────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Options ──────────────────────────────────────────────────────────────────────────╮
    │ --version         -v                 Show version.                                 │ 
    │ --slash-notation  -sn       INTEGER  Slash notation. [default: 24]                 │
    │ --subnets         -s        INTEGER  Number of subnets. [default: 2]               │
    │ --host-id-bits    -hid      INTEGER  Number of host id bits. [default: 8]          │
    │ --help                               Show this message and exit.                   │
    ╰────────────────────────────────────────────────────────────────────────────────────╯
    ```
4. Example output for `scalc 193.64.33.0 -s 4`:
    | Subnet | Network Address | Slash Notation | First Usable IP Address | Last Usable IP Address | Broadcast Address |
    |-|-|-|-|-|-|
    | 1 | `193.64.33.0` | `/26` | `193.64.33.1` | `193.64.33.62` | `193.64.33.63` |
    | 2 | `193.64.33.64` | `/26` | `193.64.33.65` | `193.64.33.126` | `193.64.33.127` |
    | 3 | `193.64.33.128` | `/26` | `193.64.33.129` | `193.64.33.190` | `193.64.33.191` |
    | 4 | `193.64.33.192` | `/26` | `193.64.33.193` | `193.64.33.254` | `193.64.33.255` |

## Current features:
- Subnet /24 notation
- Generate markdown tables of subnet information
- ...

## Planned features:
- Subnet other notations e.g. /25, /16
- ...

## Contribution
Feel free to create a pull request and add some new features or clean up the code (I know it's a bet messy). Any help is appreciated.
