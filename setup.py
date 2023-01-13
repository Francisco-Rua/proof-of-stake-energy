from setuptools import setup, find_packages

setup(
    name="pos_env",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "datetime",
        "numpy",
        "matplotlib",
        "seaborn",
        "scipy",
        "scikit-learn",
        "ipython",
        "ipykernel",
        "sklearn",
    ],
    extras_require={"dev": ["pylint", "black"]},
)
