import marimo

__generated_with = "0.10.19"
app = marimo.App(width="medium", layout_file="layouts/slides.slides.json")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        # To the Moon and back

        Juan Luis Cano Rodríguez <hello@juanlu.space>

        2025-02-04 @ PyData Prague
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Outline

        1. Introduction 🌌
        2. How it all started 🐤
        3. The Golden Era ❤️
        4. How it all ended 🪦
        5. Lessons 👴
        6. Conclusions/The future/Farewell?
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Intro

        Juan Luis (he/him/él 🇪🇸)

        - Aerospace Engineer passionate about tech communities and sustainability ♻️
        - Product Manager at QuantumBlack, AI by McKinsey, for Kedro, an open source pipeline framework 🥑
        - Organizer of the PyData Madrid monthly meetup (ex Python España, ex PyCon Spain) 🐍
        - Contributor to the SciPy and PyData ecosystem 🧪
        - Music lover 🎵

        Follow me! ::octicon:mark-github-16:: [github.com/astrojuanlu](https://github.com/astrojuanlu)

        ![Mini Juanlu](public/minijuanlu.png)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## The project

        poliastro ~~is~~ was a Python library for interactive Astrodynamics

        <img src="public/logo-poliastro-text.svg" width="600" />

        **Physics → Mechanics → Celestial Mechanics → Astrodynamics** (aka Orbital Mechanics)

        > A branch of Mechanics (itself a branch of Physics) that studies practical problems regarding the motion of rockets and other human-made objects through space.

        - Pure Python, accelerated with numba
        - MIT license (permissive) https://github.com/poliastro/poliastro/
        - Physical units, astronomical scales and more, thanks to Astropy
        - Conversion between several orbit representations
        - Analytical and numerical propagation
        - Cool documentation 🚀 https://docs.poliastro.space/
        """
    )
    return


@app.cell
def _(mo):
    import warnings

    from astropy import units as u
    from astropy.time import Time

    from poliastro.bodies import Earth
    from poliastro.twobody import Orbit

    mo.show_code()
    return Earth, Orbit, Time, u, warnings


@app.cell
def _(Earth, Orbit, Time, mo, u):
    r = [-6045, -3490, 2500] << u.km
    v = [-3.457, 6.618, 2.533] << u.km / u.s

    orb = Orbit.from_vectors(Earth, r, v, Time.now())
    mo.show_code(orb)
    return orb, r, v


@app.cell
def _(mo, orb):
    mo.show_code(orb.plot(label="Sample orbit"))
    return


@app.cell
def _(Time, mo):
    from poliastro.plotting.misc import plot_solar_system

    plotter = plot_solar_system(epoch=Time.now().tdb, outer=False, use_3d=True, interactive=True)
    mo.show_code(plotter.show())
    return plot_solar_system, plotter


@app.cell
def _(Earth, mo):
    from poliastro.bodies import Mars
    from poliastro.plotting.porkchop import PorkchopPlotter
    from poliastro.util import time_range
    import matplotlib.pyplot as plt

    launch_span = time_range("2005-04-30", end="2005-10-07")
    arrival_span = time_range("2005-11-16", end="2006-12-21")

    _, ax = plt.subplots(figsize=(10, 7))

    porkchop_plot = PorkchopPlotter(Earth, Mars, launch_span, arrival_span, ax=ax)
    porkchop_plot.porkchop()
    mo.show_code(ax)
    return (
        Mars,
        PorkchopPlotter,
        arrival_span,
        ax,
        launch_span,
        plt,
        porkchop_plot,
        time_range,
    )


@app.cell
def _(mo):
    mo.md(r"""...and much more! https://docs.poliastro.space/en/stable/gallery.html""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # How it all started

        A beautiful mess of Python, Fortran, and GNU Octave scripts... And it worked!

        ![poliastro first commit](public/poliastro-first-commit.png)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        - **0.1** _(2013)_, dropped Octave, just Python + Fortran!
        - **0.2** _(2014)_, refactored API inspired by Helge Eichhorn's project called Plyades
        - **0.3** _(2015)_, replaced Fortran with Numba, became a pure Python package!

        Cano Rodríguez, J. L. , Eichhorn, H., & McLean, F. (2016). Poliastro: an astrodynamics library written in Python with Fortran performance. In 6th International Conference on Astrodynamics Tools and Techniques. https://indico.esa.int/event/111/contributions/393/
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## But why not `<X>`?

        - Some GUI-based programs existed, but they were commercial (and expensive) or really bad
        - Some well maintained frameworks existed, but they were written in Java (and I wasn't familiar with it)
        - Some other Python libraries existed, but they weren't very well maintained (still at the "collection of scripts" stage)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## But why not join forces with `<Y>`!?

        And yet, a few well-maintained, small Python libraries existed!

        But _I still wanted to build my own_, because

        - It was fun
        - Building = Learning
        - _Starting_ something is easy at first! (More on this later)
        - I had ideas of my own that I wanted to explore freely
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Fun fact, we actually tried to coordinate! https://github.com/OpenAstrodynamics

        But the effort mostly died off almost the first week because the 3 of us couldn't agree on one thing I don't remember.

        Collaboration, cooperation, coordination are hard because they're human problems ("I/O-bound") and not technical problems ("CPU-bound").
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        # The Golden Era

        - 1x Summer of Code in Space, 5x Google Summer of Code (~3k€ each year for students)
        - Became NumFOCUS-affiliated, received 2x Small Development Grants
        - Worked as Astropy core developer for 6 months (`astropy.coordinates` and `astropy.units`)
        - Collaborated with the Libre Space Foundation
        - Presented at EuroPython 2016, Open Source Cubesat Workshop 2017, EuroSciPy 2019, SciPy US 2022
        - Had lots of fun

        ![Juanlu at ESA](public/juanlu_esa.jpg)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        Jorge, GSOC 2019 student, became a maintainer and a friend ❤️

        <img src="public/juanlu-jorge-oscw19.jpg" width=800 alt="Juanlu and Jorge at OSCW 2019 in Athens" />
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""And now, for the sad part...""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # How it all ended

        ## No itch to scratch

        - After I finished my studies, I stopped using it
        - What used to be fun became a chore
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Stuck in a local optimum

        - `astropy.units` was too slow https://github.com/astrojuanlu/fastunits/
        - `astropy.coordinates` was too complex https://github.com/astrojuanlu/astropy/commit/f7873c5a
        - `numpy` had too much overhead for small arrays https://github.com/pleiszenburg/bulk_propagate/blob/master/test_notation.ipynb
        - `numba` prevented writing high level code https://github.com/numba/numba/issues/2952
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## "Companies don't want to give back!"

        - **Open source is open source**: Companies don't _have_ to give back
        - But the minimal currency in open source is a very cheap one: attribution and acknowledgement

        <img src="public/no-testimonial.png" width="600" />
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        Instead of whining, it's on _us_ to figure out a business model.

        And, mind you, **open source is a channel, not a business model**!

        Watch Adam Jacob's talk, that's it 👇

        <iframe width="560" height="315" src="https://www.youtube.com/embed/rmhYHzJpkuo?si=0_gS_uordXsoN1xk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Space != Space industry

        In the same way that Music != Music industry

        ![Guy from the record company](public/ray-foster.jpg)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        For starters, "The Commercial Satellite Imagery Business Model is Broken" https://joemorrison.substack.com/p/the-commercial-satellite-imagery

        <img src="public/satellite-imagery-business.png" width=800 alt="Commercial Satellite Imagery Business Model in a picture" />
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        And if that wasn't bad enough...

        ![Elon Musk](public/elon-musk.png)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        In the end, stepped down 😢

        https://www.poliastro.space/blog/2022/12/21/juan-luis-steps-down/

        ![Juanlu steps down](public/juanlu-steps-down.png)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Lessons

        1. Open source is the most awesome way of developing software ❤️
        2. If you are doing it for fun, ensure it stays fun!
            - And the moment it's not, it's okay to let go
        3. Giving back is not, and can never be, a condition for consuming open source, and maintainers have to come to terms with that
            - Whoever doesn't like it, should figure out a business model, do something else, or risk burning out!
        4. Great projects eventually require quality time, which in turn require either money, or personal sacrifice
            - And personal sacrifice is not sustainable in the long run
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        Despite the sad ending, was it all worth it?

        **Yes ❤️‍🔥**

        It was quite a ride. I learned a ton. I made new friends. I traveled around the world. And I gave back to the community.

        Not many people have the privilege to even devote time to creating open source. I feel truly fortunate of having done this.

        The old needs to give way to the new.

        Thank you, gracias, grazie!

        <hello@juanlu.space>

        2025-02-04 @ PyData Prague
        """
    )
    return


if __name__ == "__main__":
    app.run()
