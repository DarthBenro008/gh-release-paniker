# The Ultimate GitHub Actions Release Repository

This repository contains various GitHub Actions that help Open-Source projects release a new version of their project with a single command. 

This repository contains the following:

- [**`rust-releaser`** ](.github/workflows/rust-releaser.yaml)
- [**`golang-releaser`**](.github/workflows/golang-releaser.yaml)
- [**`hugo-releaser`**](.github/workflows/hugo-releaser.yaml)
- [**`android-releaser`**](.github/workflows/android-releaser.yaml)

## Use Cases

| Workflow Name    | Description                                                                                            | Builds and releases across multiple OS/Platforms in a single command | What triggers the workflow?                                          |
|------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| rust-releaser    | Release your rust based application across linux, windows, macOS in a single command with changelogs   | Yes                                                                  | on push of tags starting with "v", eg: v1.0, v0.1.1                  |
| golang-releaser  | Release your Golang based application across linux, windows, macOS in a single command with changelogs | Yes                                                                  | on push of tags starting with "v", eg: v1.0, v0.1.1                  |
| hugo-releaser    | Release your Hugo website to GitHub pages in a single command                                          | Yes                                                                  | on push to master/main branch                                        |
| android-releaser | Build, Release and Test your android app and get it delivered on Telegram Channel of your choice       | Yes                                                                  | on push to master/main branch, and on push of tags starting with "v" |

## GitHub Actions featured in this repository

- actions/checkout@v1
- actions-rs/toolchain@v1
- actions/setup-go@v2
- softprops/action-gh-release@v1
- peaceiris/actions-hugo@v2
- peaceiris/actions-gh-pages@v3
- DarthBenro008/app-brickie@v3.1

