# dungeon-revealer Game System Notes

A repository of notes ready to import into [dungeon-revealer](https://github.com/dungeon-revealer/dungeon-revealer/). The main purpose of this repository is to host system reference documents of role playing games.


- [Dungeon Revealer](notes/Dungeon%20Revealer/wiki)
  - [Wiki][dungeon-revealer-wiki]
- [Dungeons and Dragons](notes/Dungeons%20and%20Dragons)
  - [5e SRD][dnd-5e-srd]



## Contributing

Pull requests are welcome! We will only accept content released under permissive licenses such as OGL, CC, etc.

1. Clone this repository: `git clone https://github.com/dungeon-revealer/game-system-notes.git`
2. Add your document files in an appropriate folder. For example: `notes/game/document/`.
  - Make sure the files you add have [appropriate headers](https://github.com/dungeon-revealer/dungeon-revealer/wiki/Notes#importing-notes) for dungeon-revealer.
  - You must also include the license of your document.
  - Do not add zip files. We have a workflow that generates the zip files.
3. Add metadata for your document in [documents.yml](documents.yml) using the following template:
```YAML
  game:
    document:
      name: Document Title
      path: path/to/folder
      zip: game-document.zip
```
4. Add your document and links to the [README](README.md). For example:

```Markdown
- [Dungeons and Dragons](notes/Dungeons%20and%20Dragons)
  - [5e SRD][dnd-5e-srd]

[dnd-5e-srd]: https://github.com/dungeon-revealer/game-system-notes/releases/download/v0.2.0/dnd-5e-srd.zip
```
5. Submit a pull request.


## TODO

- [x] Lint documents in PRs.
- [ ] Automatically generate the link tree in the README.
- [ ] Add more [SRDs](https://www.dicegeeks.com/rpg-srds/).

[dnd-5e-srd]: https://github.com/dungeon-revealer/game-system-notes/releases/download/v0.2.0/dnd-5e-srd.zip
[dungeon-revealer-wiki]: https://github.com/dungeon-revealer/game-system-notes/releases/download/v0.2.0/dungeon-revealer-wiki.zip