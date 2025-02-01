import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


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

        1. Introduction :galaxy:
        2. How it all started :little_chicken:
        3. The Golden Era :heart:
        4. How it all ended :tomb:
        5. Lessons :old_man:
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

        poliastro is a (former) Python library for interactive Astrodynamics

        > The branch of Mechanics that studies...

        - Summary of features
        - Last ever released version
        - Demo!
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # How it all started

        (Do I have the Venus report somewhere? That would be fun to show)

        (Or maybe the email from my Italian friend giving up, maybe in `juanlu001@gmail.com`)

        (And also at some point Vallado's screenshot, so that I can share the last one again)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        - First, basically a collection of scripts
        - poliastro 0.1, yay it's a library! (works on my machine)
        - poliastro 0.2, ?
        - ...
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
        Fun fact, we actually tried to coordinate! `OpenAstrodynamics`

        But the  effort died almost the first week because the 3 of us couldn't agree on one thing I don't remember.

        Collaboration, cooperation, coordination are hard because they're human problems ("I/O-bound") and not technical problems ("CPU-bound").
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        # The Golden Era

        - 1x Summer of Code in Space, 4x Google Summer of Code (~10 k€ for students)
        - NNN releases
        - Became NumFOCUS-affiliated
        - ...

        (Not the part you came to learn about :wink:)
        """
    )
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
        r"""
        _Brainstorming of factors_ before I describe them in detail:

        - Stopped using it (no more fun)
        - Technical barriers became trickier, focus time was needed (no more "easy")
            - API design is actually hard
            - ~~Some abstractions were difficult to evolve~~
                - Too generic?
            - ~~Generalising Earth capabilities created tension~~
                - Too niche perhaps
            - Saturated what the dependencies could do, and ad-hoc solutions were needed, which required time
                - numba couldn't be any faster, code became too Fortran-esque
                - astropy.units and astropy.coordinates were too slow
                - small NumPy arrays weren't the right choice for some tasks
            - How could I get that focus time? By getting paid, but only my students were getting paid, remember?
            - If only some companies were using it...
        - "Companies don't want to give back!" (no more rewarding)
            - The anecdote with Spire
            - So for the first time I felt resentment! It was very irrational, but also very real
        - The space industry basically became shit, I quit in early 2021 (no more fulfilling)
            - Elon Musk
            - But also... social impact was a lie https://joemorrison.substack.com/p/a-simple-mental-model-for-understanding

        All of it is in https://www.poliastro.space/blog/2022/12/21/juan-luis-steps-down/ (which can be presented later)

        (Be careful because this part can become super boring and detail)

        (Although it would actually be good to establish a parallelism between these 4 motives and the intrinsic/extrinsic motivations at the very beginning)
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""In the end, stepped down :sad:""")
    return


@app.cell
def _(mo):
    mo.md(
        """
        # Lessons

        1. Giving back is not, and can never be, a condition for consuming open source, and maintainers have to come to terms with that
            - Whoever doesn't like it, should just do something else, or risk burning out!
        2. Great projects eventually require quality time, which in turn require either money, or personal sacrifice
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""On the topic of money and open source... Just watch Adam Jacob's talk, that's it""")
    return


@app.cell
def _(mo):
    mo.md(
        """
        Despite the sad ending, it was quite a ride. I learned a ton. I made new friends. I traveled around the world. And I gave back to the community.

        Not many people have the privilege to even devote time to creating open source.

        I feel truly fortunate of having done this.

        And the old needs to give way to the new.

        Thank you, gracias, grazie :heart:
        """
    )
    return


if __name__ == "__main__":
    app.run()
