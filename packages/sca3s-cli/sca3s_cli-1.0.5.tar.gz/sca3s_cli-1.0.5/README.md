# [SCA3S](https://github.com/scarv/sca3s): command-line interface

<!--- -------------------------------------------------------------------- --->

*Acting as a component part of the wider
[SCARV](https://www.scarv.org)
project,
SCA3S is a collection of resources that support the development 
and analysis of cryptographic implementations wrt.
[side-channel attack](https://en.wikipedia.org/wiki/Side-channel_attack):
SCA3A is, more specifically, pitched as offering
"side-channel analysis as a service":
it allows users to acquire and analyse side-channel data-sets which stem 
from execution of their implementation, without (necessarily) owning or 
operating the associated infrastructure.
Mirroring the goals of SCARV, it places particular emphasis on analogue 
side-channels (e.g., power and EM) stemming from
[RISC-V](https://riscv.org)-based
platforms.
The main
[repository](https://github.com/scarv/sca3s)
acts as a general container for associated resources;
this specific submodule houses
a [CLI](https://en.wikipedia.org/wiki/Command-line_interface) which allows interaction with the front-end infrastructure without using the web-based UI.*

<!--- -------------------------------------------------------------------- --->

## Organisation

```
├── bin                     - scripts (e.g., environment configuration)
├── build                   - working directory for build
├── extern                  - external resources (e.g., submodules)
│   └── wiki                  - submodule: scarv/sca3s-cli.wiki
└── src
    └── sca3s
        └── cli
```

<!--- -------------------------------------------------------------------- --->

## Installation 

```bash
pip install sca3s_cli
```

## Configuration

- SCA3S CLI links to a pre-existing SCA3S account via an API token which can be obtained via the user profile page.
- Once a token is obtained and `sca3s-cli` installed, edit the config file in `~/.sca3s/config` as follows:

```bash
[default]
token
```

This will link the cli to your SCA3S account. If you possess multiple SCA3S accounts you can add additional tokens
with friendly names to the config file and utilise these tokens via the `scope` parameter in the cli.

<!--- -------------------------------------------------------------------- --->

## Questions?

- read the
  [wiki](https://github.com/scarv/sca3s-cli/wiki),
- raise an
  [issue](https://github.com/scarv/sca3s-cli/issues),
- raise a
  [pull request](https://github.com/scarv/sca3s-cli/pulls),
- drop us an 
  [email](mailto:sca3s@scarv.org).

<!--- -------------------------------------------------------------------- --->

## Acknowledgements

This work has been supported in part 

- by EPSRC via grant 
  [EP/R012288/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R012288/1) (under the [RISE](https://www.ukrise.org) programme), 
  and 
- by the
  [AWS Cloud Credits for Research](https://aws.amazon.com/research-credits)
  programme.

<!--- -------------------------------------------------------------------- --->

