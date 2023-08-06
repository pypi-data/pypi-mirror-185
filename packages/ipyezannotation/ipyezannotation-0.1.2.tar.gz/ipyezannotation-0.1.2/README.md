# Easy Annotation

**ipyezannotation** - Easy, simple to customize, pythonic data annotation framework.

# Disclaimer

This project is in early development stage, so don't blame me if it opens-up a black hole in your HDD 😄, 
other than that **IT WORKS!** 🥳

Docs & examples coming soon.

# Dependencies

This project currently supports `Python>=3.8`.

# Installation

There are two options to install this project:

- Download and install from PyPI by simply running: `pip install ipyezannotation` & you're done!
- Alternatively, install from source using Poetry. This project uses `poetry>=1.3` to manage dependencies.

# Examples

## Images selection annotation

Annotation using `ImageSelectAnnotator`.

Define data to annotate with `ImageSelectAnnotator`:

```python
source_groups = [
    ["./surprized-pikachu.png"] * 16,
    ["./surprized-pikachu.png"] * 7,
    ["./surprized-pikachu.png"] * 8,
    ["./surprized-pikachu.png"] * 4,
]
```

Convert input data to `Sample`'s:

```python
from ipyezannotation.studio.sample import Sample, SampleStatus

samples = [
    Sample(
        status=SampleStatus.PENDING,
        data=group,
        annotation=None
    )
    for group in source_groups
]
```

Initialize database of your liking and synchronize it with your new input samples:

```python
from ipyezannotation.studio.storage.sqlite import SQLiteDatabase

db = SQLiteDatabase("sqlite:///:memory:")
synced_samples = db.sync(samples)
```

Configure & create annotation `Studio` to label your samples:

```python
from ipyezannotation.studio import Studio
from ipyezannotation.annotators import ImageSelectAnnotator

Studio(
    annotator=ImageSelectAnnotator(n_columns=8),
    database=db
)
```

![](./examples/image-select-annotation/output.png)
