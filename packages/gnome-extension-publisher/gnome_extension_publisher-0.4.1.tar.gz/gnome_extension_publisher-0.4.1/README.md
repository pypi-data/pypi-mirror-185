# Gnome Extension Publisher
Tool to upload Gnome-Shell extensions to [extensions.gnome.org](https://extensions.gnome.org).

This is a fork of 'gnome-extension-publisher' which seems to be abandoned.

## Install
```console
pip install gnome-extension-publisher
```

## How to use
```console
gep build # runs glib-compile-schemas and builds the zip file
gep publish --username <YOUR_EXTENSIONS_GNOME_ORG_USERNAME> --password <YOUR_EXTENSIONS_GNOME_ORG_PASSWORD>
gep --help # for help :)
```

You can also provide your username and password via environment variables (GEP_USERNAME, GEP_PASSWORD).

## Use in Gitlab CI/CD
Add GEP_USERNAME and GEP_PASSWORD to your build variables in your repository settings.

This will publish every tag on [extensions.gnome.org](https://extensions.gnome.org)
```yaml
stages:
  - publish

production:
  image: python:3.8.3-buster
  stage: publish
  script:
    - pip install gnome-extension-publisher
    - gep publish
  only:
    - tags
```

## Support
Feel free to submit a pull request