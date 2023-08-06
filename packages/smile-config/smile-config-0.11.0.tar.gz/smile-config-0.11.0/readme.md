
# Table of Contents

1.  [Install](#org5b37d13)
2.  [Usage](#org0e93884)
    1.  [Dataclass to command line options](#orgfa7358a)
        1.  [Simple types](#org4a8ecad)
        2.  [Complex types](#orgd46e562)
        3.  [Nested dataclass](#org1bb2431)
    2.  [APIs](#orgec9b8e0)
        1.  [Example](#orgbfda407)

Generate command line options  from dataclasses.

    # config.py
    from dataclasses import dataclass, asdict, field
    from smile_config import from_dataclass
    
    @dataclass
    class Train:
        """Train config."""
    
        batch_size: int = 64
    
    
    @dataclass
    class ML:
        lr: Annotated[float, dict(help="learning rate", type=float)] = 0.001
        train: Train = Train()
        cc: list[int] = field(default_factory=lambda: [10])
    
    
    @dataclass
    class Example:
        """Example config."""
    
        ml: ML = ML()
        x: bool = True
        a: int | None = None
    
    config = from_dataclass(Example()).config
    
    print(config)
    
    # If autocomplete is not working, try to add the following line to your config file:
    from typing import cast
    config = cast(Example, config)

You can access the config as namedtuple.

    > python config.py --ml.cc 10 10 --ml.lr 0.001 --no-x --a "1"
    Example(ml=ML(lr=0.001, train=Train(batch_size=64), cc=[10, 10]), x=False, a=1)

Also, auto generate help message with default value.

    > python config.py
    usage: collections.py [-h] [--ml.lr ML.LR] [--ml.train.batch_size ML.TRAIN.BATCH_SIZE] [--ml.cc ML.CC [ML.CC ...]] [--x | --no-x] [--a A]
    
    Example config.
    
    options:
      -h, --help            show this help message and exit
      --x, --no-x           - (default: True)
      --a A                 - (default: None)
    
    ml:
      --ml.lr ML.LR         learning rate (default: 0.001)
      --ml.cc ML.CC [ML.CC ...]
                            - (default: [10])
    
    ml.train:
      --ml.train.batch_size ML.TRAIN.BATCH_SIZE
                            - (default: 64)


<a id="org5b37d13"></a>

# Install

    pip install -U smile_config


<a id="org0e93884"></a>

# Usage


<a id="orgfa7358a"></a>

## Dataclass to command line options


<a id="org4a8ecad"></a>

### Simple types

Everything that argpase can handle.  `int`, `float`, `str`, `bool`, and callable object.

    @dataclass
    class Simple:
        a: int = 1
        b: float = 2.0
        c: str = "hello"
        d: bool = False
        e: list[int] = field(default_factory=lambda: [10])

Will convert to:

    parser.add_argument("--a", help="-", type=int, default=1)
    parser.add_argument("--b", help="-", type=float, default=2.0)
    parser.add_argument("--c", help="-", type=str, default="hello")
    parser.add_argument("--d", help="-", type=bool, default=False, action="store_true")
    parser.add_argument("--e", help="-", type=int, default=[10], nargs="+")


<a id="orgd46e562"></a>

### Complex types

Smile config uses `Annotation` to handle complex types, which will pass
the second argument to `parser.add_argument`.

    @dataclass
    class C:
        x: Annotated[int, "Helps for x."] = 1

See the logic here:

The first argument is the type, e.g. `int`.

if the second argument is `str`, e.g. `s`, it will be passed as `parser.add_argument("--x", help=s, ...)`.

If the second argument is a `list`, e.g. `args`, it will be passed as `parser.add_argument("--x", ..., *args)`.

If the second argument is a `dict`, e.g. `kwds`, it will be passed as `parser.add_argument("--x", ..., **kwds)`.


<a id="org1bb2431"></a>

### Nested dataclass

Of course! It does support nested dataclass.

    @dataclass
    class A:
        a: int = 1
    
    @dataclass
    class B:
        a: A = A()
    
    @dataclass
    class C:
        a: A = A()
        b: B = B()
        c: int = 0
    
    
    print(from_dataclass(C()).config)
    
    # Output:
    # C(a=A(a=1), b=B(a=A(a=1)), c=0)


<a id="orgec9b8e0"></a>

## APIs

Smile config provides four APIs:

    class Config:
    
        # the dataclass dict
        self.conf
    
        # the dataclass
        self.config
    
    # Generate command line options from dataclass.
    # For formatter: `from rich_argparse import RichHelpFormatter`
    # `ns`: namespaces for types.
    def from_dataclass(dc: Dataclass, *, formatter: HelpFormatter = RichHelpFormatter, ns: dict | None = None) -> Config:...
    
    # Convert dict to an existing dataclass
    def from_dict(dc: Type[Dataclass], d: dict) -> Dataclass:...
    
    # Merge a dict with an existing dataclass instance
    def merge_dict(dc: Dataclass, d: dict) -> Dataclass:...


<a id="orgbfda407"></a>

### Example

    @dataclass
    class Eg:
        a: int = 1
        b: bool = False
    
    conf = from_dataclass(Eg())
    
    print(conf)  # Config
    # output: Eg(a=1, b=False)
    
    print(conf.conf)  # dict
    # output: {'a': 1, 'b': False}
    
    print(conf.config)  # Eg
    # output: Eg(a=1, b=False)
    
    conf_dc = from_dict(Eg, {"a": 2, "b": True})  # Type[Eg] -> dict -> Eg
    print(conf_dc)
    # output: Eg(a=2, b=True)
    
    conf_merge = merge_dict(conf_dc, {"a": 3})  # Eg -> dict -> Eg
    print(conf_merge)
    # output: Eg(a=3, b=True)

