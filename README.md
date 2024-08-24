# canvas-api-project

Designing a set of scripts to automate interactions with Canvas, so
that I can do things over the course of a semester without having to
worry too much about the point-click-point-click of it.

## Quick start

To get going

```
$ eval $(pdm venv activate in-project)
```

## Dependencies

Add new dependencies for development to Group 'test'

```
pdm add -dG test foo
```

List dependencies and their sub-dependency relationships

```
pdm list --tree
```

## API Documentation/interaction

- [Fantastic resource for getting started](getting-started)

- [Live API on test environment](https://setonhall.test.instructure.com/doc/api/live)

- [With this Python library, the programming becomes trivial](https://canvasapi.readthedocs.io/)


[getting-started]: https://community.canvaslms.com/t5/Canvas-Developers-Group/Canvas-APIs-Getting-started-the-practical-ins-and-outs-gotchas/ba-p/263685
