# A many-in-one tool for managing your Markup Language files.

## What is it?

**iotre** is a tool for managing your Markup Language files. It is capable to write and read files in the following formats:

- JSON
- YAML
- TOML
- XML
- And soon more... :wink:

The basic goal was to have a small package anyone could add to their project and use it to manage their files. It is also possible to use it as a CLI tool.

## Installation

You cannot install the CLI tool separately for now. You can install it with the following command:

```bash
pip install iotree
```

## Usage

### As a CLI tool

To see what the display function can do, you can use the following command:

```bash
iotree demo
```

For example, the following JSON file (displayed in VSCode)

![JSON file](https://i.imgur.com/N4iKgMJ.png)

will be displayed like this:

![JSON file displayed](https://i.imgur.com/tUSyW3L.png)

While the following YAML file (displayed in VSCode)

![YAML file](https://i.imgur.com/UE4ZxuQ.png)

will be displayed like this:

![YAML file displayed](https://i.imgur.com/t3q5yHS.png)

**Note**: The CLI tool is not yet finished. It is still in development.  
If this just looks like a wrapper around [rich trees](https://rich.readthedocs.io/en/stable/tree.html)) to you, it almost because it is. :wink:

As a CLI tool, the key difference I want to bring is the ability to configure *themes* and *styles*.

Just run the following command to interactively create a theme:

```bash
iotree config init
```

But if you're lazy, just use a file:

```bash
iotree config init from-json my_theme.json
```

For example, the following JSON file

```json
{   
    "name": "My super pseudonym",
    "username": "my.username",
    "symbol": "lgpoint",
    "theme": "bright-blue-green"
}
```

will result in the following theme: ... 
