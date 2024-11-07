from manim import *


class Sets(Scene):
    def construct(self):
        # Title text
        title = Title("Sets", color=ORANGE)

        # MathTex object for the set notation
        sets = MathTex(r"A = \{a_1, a_2, a_3, \ldots, a_n\}", font_size=40)

        # Save the original state
        sets.save_state()

        # Animate the title and the set notation
        self.play(Create(title), run_time=1.5)
        self.wait(1.5)

        self.play(Write(sets), run_time=1.5)
        self.wait(1.5)

        # Target the curly braces and other parts for transformations
        opening_brace = sets.get_part_by_tex(r"\{")
        closing_brace = sets.get_part_by_tex(r"\}")

        self.play(
            opening_brace.animate.set_opacity(
                0.2
            ),  # Lower opacity of the opening brace
            closing_brace.animate.set_opacity(
                0.2
            ),  # Lower opacity of the closing brace
            sets[0][0].animate.scale(1.2),  # Scale 'A'
            run_time=1.5,
        )
        self.wait(1.5)

        # Restore to the original state
        self.play(Restore(sets), run_time=1.5)
        self.wait(1.5)

        # Another animation targeting different parts
        self.play(
            sets[0][0:2:1].animate.set_opacity(0.2),  # Lower opacity for "A ="
            sets[0][2:].animate.scale(1.2),  # Scale " {a_1,a_2,a_3,...,a_n}"
            run_time=1.5,
        )
        self.wait(1.5)

        self.play(
            sets[0][2].animate.set_color(ORANGE),
            sets[0][len(sets[0]) - 1].animate.set_color(ORANGE),
            run_time=1.5,
        )

        self.wait(1.5)

        self.play(
            sets[0][2].animate.set_color(WHITE),
            sets[0][len(sets[0]) - 1].animate.set_color(WHITE),
            sets[0][3 : len(sets[0]) - 1].animate.set_color(ORANGE),
            run_time=1.5,
        )

        self.wait(1.5)

        self.play(Restore(sets), run_time=1.5)

        self.wait(1.5)

        self.play(FadeOut(sets), run_time=1.5)
        self.wait(1.5)

        # Example Set {3,7}
        exampleSet = MathTex(
            r"\{3,7\} =", r"\{7,3\} ", r"= \{7,7,3\} =", r"\{7,3,3\}", font_size=40
        )

        self.play(Write(exampleSet[0:2]), run_time=1.5)

        self.wait(1.5)

        self.play(FadeIn(exampleSet[2:4]), run_time=1.5)

        self.wait(1.5)

        self.play(Uncreate(exampleSet), run_time=1.5)

        self.wait(1.5)

        # FamousSets
        naturalSet = MathTex(r"\mathbb{N} = \{1,2,3,\ldots\}", font_size=40)
        integerSet = MathTex(
            r"\mathbb{Z} = \{\ldots,-3,-2,-1,0,1,2,3,\ldots\}", font_size=40
        )
        rationalSet = MathTex(
            r"\mathbb{Q} = \{\frac{a}{b} \;|\; a\in \mathbb{Z}, b\in \mathbb{Z}\backslash\{0\}\}",
            font_size=40,
        )
        realSet = MathTex(r"\mathbb{R} = \{x \;|\; -\infty <x<\infty\}")

        famousSets = VGroup(naturalSet, integerSet, rationalSet, realSet).arrange(
            DOWN, buff=1
        )
        self.play(Write(famousSets[0]), run_time=1.5)

        self.wait(1.5)

        self.play(Write(famousSets[1]), run_time=1.5)

        self.wait(1.5)

        self.play(Write(famousSets[2]), run_time=1.5)

        self.wait(1.5)

        self.play(Write(famousSets[3]), run_time=1.5)

        self.wait(1.5)

        self.play(FadeOut(famousSets), run_time=1.5)

        self.wait(1.5)

        # Set = (10,infinity)
        newSet = MathTex(r"B = \{x\; | \; x>10\}", font_size=40)

        newSet.save_state()

        self.play(Write(newSet), run_time=1.5)

        self.wait(1.5)

        self.play(
            newSet.animate.set_opacity(0.2),
            newSet[0][4].animate.scale(1.2).set_opacity(1),
            run_time=1.5,
        )

        self.wait(1.5)

        self.play(Restore(newSet), run_time=1.5)

        self.wait(1.5)

        self.play(FadeOut(newSet))

        numLine = NumberLine(length=10, include_tip=True, x_range=[7, 18, 1])

        self.play(Create(numLine), run_time=1.5)

        self.wait(1.5)

        # Create labels for numbers greater than 10 and place them above the number line
        labels = VGroup()
        labels.add(Text(str(10), font_size=24).next_to(numLine.n2p(10), UP))
        for x in range(11, 19, 1):  # Start from 11 to 19 with step of 1

            if x < 15:
                label = Text(str(x), font_size=24).next_to(numLine.n2p(x), UP)
                labels.add(label)
                # Position above
            else:
                label = MathTex(r"\cdot", font_size=40).next_to(
                    numLine.n2p(x), UP
                )  # Position below
                labels.add(label)

        exclude_dot = Dot(
            numLine.n2p(10),  # Position the dot at 10 on the number line
            color=YELLOW,  # Color of the dot
            fill_opacity=0,  # Make it hollow
            stroke_width=3,  # Border width
        )
        labels.add(exclude_dot)

        # Animate the appearance of labels
        self.play(FadeIn(labels), run_time=1.5)
        self.wait(1.5)


class LogicalOperators(Scene):
    def construct(self):
        title = Title("Logical Operators", color=ORANGE)
        self.play(Create(title), run_time=1.5)
        self.wait(1.5)

        # Implies
        aImpliesB = MathTex(r"A \Rightarrow B", font_size=40).shift(UP).save_state()

        implyExample1 = Tex(
            "You studies hard $\Rightarrow$  You get a high grade",
            font_size=40,
        ).move_to(aImpliesB, DOWN)
        implyExample2 = Tex(
            "You get a high grade $\\nRightarrow$ You studies hard", font_size=40
        ).move_to(implyExample1, DOWN)

        implyExample = VGroup(implyExample1, implyExample2).arrange(DOWN, buff=1)

        self.play(Write(aImpliesB), run_time=1.5)
        self.wait(1.5)

        self.play(aImpliesB[0][1].animate.set_color(ORANGE), run_time=1.5)
        self.wait(1.5)

        self.play(Uncreate(aImpliesB), run_time=1.5)
        self.wait(1.5)

        self.play(Write(implyExample[0]), run_time=1.5)
        self.wait(1.5)

        self.play(FadeIn(implyExample[1]), run_time=1.5)
        self.wait(1.5)

        self.play(FadeOut(implyExample), run_time=1.5)
        self.wait(1.5)

        # NOT B IMP NOT A
        ANB = MathTex(
            r"\lnot B \Rightarrow \lnot A\qquad",
            r"\text{not } B \Rightarrow \text{not } A",
            font_size=40,
        ).shift(UP)

        self.play(Write(ANB), run_time=1.5)
        self.wait(1.5)

        self.play(Uncreate(ANB), run_time=1.5)
        self.wait(1.5)

        ANBExample = Tex(
            "You didn't get a high grade $\\nRightarrow$ You didn't study hard",
            font_size=40,
        )
        self.play(Write(ANBExample), run_time=1.5)
        self.wait(1.5)

        self.play(FadeOut(ANBExample))

        # IFF
        aIffB = MathTex(r"A \iff B", font_size=40).shift(2 * UP).save_state()
        self.play(Write(aIffB), run_time=1.5)
        self.wait(1.5)

        self.play(aIffB[0][1:3].animate.set_color(ORANGE), run_time=1.5)
        self.wait(1.5)

        self.play(Uncreate(aIffB))

        self.wait(1.5)

        iffExample1 = Tex(
            "A tall person $\iff$ His/Her height is bigger than 160 cm", font_size=40
        ).move_to(aIffB, DOWN)
        iffExample2 = Tex(
            "A tall person $\Longrightarrow$  His/Her height is bigger than 160 cm",
            font_size=40,
        )
        iffExample3 = Tex(
            "His/Her height is bigger than 160 cm $\Longrightarrow$ A tall person",
            font_size=40,
        )
        iffExample = (
            VGroup(iffExample2, iffExample3)
            .arrange(DOWN, buff=1)
            .move_to(ORIGIN + 0.5 * DOWN)
        )

        self.play(Write(iffExample1), run_time=1.5)
        self.wait(1.5)

        self.play(Write(iffExample[0]), run_time=1.5)
        self.wait(1.5)

        self.play(Write(iffExample[1], run_time=1.5))
        self.wait(1.5)

        self.play(FadeOut(iffExample), FadeOut(iffExample1), run_time=1.5)

        mathExample1 = MathTex(r"x+3 = 14", r" \iff ", r"x = 11", font_size=40).move_to(
            aIffB, DOWN
        )

        self.play(Write(mathExample1), run_time=1.5)
        self.wait(1.5)

        mathExample2 = MathTex(
            r"x+3 = 14",
            r" \Longrightarrow ",
            r"x = 11",
            r"\quad \text{ is also correct}",
            font_size=40,
        ).shift(UP)

        self.play(Write(mathExample2), run_time=1.5)
        self.wait(1.5)

        self.play(Uncreate(mathExample1), Uncreate(mathExample2), run_time=1.5)
        self.wait(1.5)


class Symbols(Scene):
    def construct(self):
        title = Title("Symbols")

        forall = MathTex(
            r"\forall:  \quad",
            r"\forall\; \text{The students in the 11th grade}",
            font_size=40,
        )
        _in = MathTex(
            r"\in: \quad",
            r"3 \in \{3,7\} \quad",
            r"\text{Romeo is $\in$ the 11th grade}",
            font_size=40,
        )
        notIn = MathTex(
            r"\notin: \quad",
            r"4 \notin \{3,7\} \quad",
            r"\text{Romeo is $\notin$ the 12th grade}",
            font_size=40,
        )
        exists = MathTex(
            r"\exists: \quad",
            r"\forall\; \text{The students in the 11th grade} \exists \text{the person with the highest grade}",
            font_size=40,
        )
        excluding = MathTex(
            r"\backslash: \quad",
            r"\{0,1,2,3\}\backslash \{0\} = \{1,2,3\}",
            font_size=40,
        )
        suchthat = MathTex(r"| : \quad", r"\{x\; |\; x>10\}", font_size=40)
        setNotation = MathTex(r"\{\ldots\}")

        self.play(Write(title), run_time=1.5)
        self.wait(1.5)

        symbols = VGroup(forall, _in, exists, excluding, suchthat, setNotation)

        for symbol in symbols:
            self.play(Write(symbol), run_time=1.5)
            self.wait(1.5)
            self.play(Uncreate(symbol), run_time=1.5)
            self.wait(1.5)

        self.play(FadeOut(title))


class Proof(Scene):
    def construct(self):
        title = Title("Proofs")
        self.play(Create(title), run_time=1.5)
        self.wait(1.5)

        question1 = (
            Tex("Question 1: $n$ is odd $\Longrightarrow n^2$ is odd", font_size=40)
            .to_edge(UL)
            .shift(DOWN)
        )
        self.play(Write(question1), run_time=1.5)
        self.wait(1.5)

        step1 = (
            MathTex(
                r"n \text{ is odd} \iff \exists k\in \mathbb{N} \text{ such that } n=2k+1",
                font_size=40,
            )
            .next_to(question1, 1.5 * DOWN)
            .align_to(question1, LEFT)
        )
        self.play(Write(step1), run_time=1.5)
        self.wait(1.5)

        step2 = (
            MathTex(r"n^2 = (2k+1)^2 = 4k^2+4k+1", font_size=40)
            .next_to(step1, 1.2 * DOWN)
            .align_to(step1, LEFT)
        )
        self.play(Write(step2), run_time=1.5)
        self.wait(1.5)

        step3 = (
            MathTex(r"4k^2+4k+1 = 2(2k^2+2k)+1", font_size=40)
            .next_to(step2, 1.2 * DOWN)
            .align_to(step2, LEFT)
        )
        self.play(Write(step3), run_time=1.5)
        self.wait(1.5)

        step4 = (
            MathTex(
                r"\text{Let } 2k^2 +2k = t \iff  2(2k^2+2k)+1 = 2t+1 \quad \blacksquare ",
                font_size=40,
            )
            .next_to(step3, 1.2 * DOWN)
            .align_to(step3, LEFT)
        )
        self.play(Write(step4), run_time=1.5)
        self.wait(1.5)

        steps1 = VGroup(question1, step1, step2, step3, step4)

        self.play(Uncreate(steps1), run_time=1)
        self.wait(1.5)

        questions2 = (
            Tex("Question 2: $n^2$ is even $\Longrightarrow n$ is even", font_size=40)
            .to_edge(UL)
            .shift(DOWN)
        )
        self.play(Write(questions2), run_time=1.5)
        self.wait(1.5)


class SqrtTwo(Scene):
    def construct(self):
        title = Title("Proving $\sqrt{2}$ is not rational", color=ORANGE)
        self.play(Write(title), run_time=1.5)
        self.wait(1.5)

        num = MathTex(r"x", r"= \frac{m}{n}", font_size=40)
        self.play(Write(num), run_time=1.5)
        self.wait(1.5)
