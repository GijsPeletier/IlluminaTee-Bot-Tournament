# Cover Bot Tournament

Welcome to the third annual Cover Bot Tournament!
We fight for sweet victory, we fight for everlasting glory, but most importantly, we fight for K.A.S.T. credit.

This year we will host two different games. One is a fan favourite: chess, the other: a mystery...

## Submitting a bot

1. Any bot that you submit will have to match the specification of an `Engine`, as implemented in the `src/definitions.py` file.
2. A bot can be submitted as a single python file or a directory.
    - Single file:
        - The bot should be implemented as a python class (or function, as long as it still matches the spec) called `ChessBot`.
        - You may not load from, or save to the disk.
    - Directory:
        - The root directory should contain a `main.py` file, which contains the `ChessBot` class (or function).
        - You can access any file inside your directory, but use relative paths. These paths should use the global constant `ROOT_DIR`, as shown in the `bots/directory_bot/main.py` example.
3. You are allowed to use three libraries. `python-chess`, `tqdm`, and `torch`. The python version will be 3.12. The torch CUDA build tag used will be `+cu128`.

## Resources

You are allotted 8 gigabytes of disk space, 4 gigabytes of RAM, and 4 gigabytes of VRAM. Assume x86 architecture. If you need more information, contact us.

note: be conservative with the resources, because exceeding your allotted time loses the game, and exceeding memory disqualifies your bot!

## Other Rules and Specifications

1. You are free to submit a bot as many times as you want, but only your most recent entry will compete.
2. We will decide the ranking of the engines by playing a Swiss tournament.
3. Each game will be played with a 5 minute time control, no increment.
4. Each game will start with an opening to prevent all games from progressing the same way.
5. Whenever an opponent can force a draw by the rules of the game (50 move rule or 3-fold repetition in chess) the game is considered to have ended by draw.
6. The initialisation of your bot can take at most 10 seconds. Updating your bot is allowed to take up to 2 minutes (see explanation below).
7. You are not allowed to use existing implementations, endgame tablebases, or opening books.
8. You are not allowed to use a bare except or to except a BaseException or KeyboardInterrupt. We will take it out.

These rules do not cover every scenario possible. To deal with this, the rules may be modified and expanded at the discretion of the Illuminatee committee. Make sure to keep an eye out for possible changes. Do you have an idea, but are you unsure of its legality? Contact us, and we will make a decision.

## The mystery

In  addition to chess, you can submit a bot to play a different game. The catch is that you will not know which game your engine will be playing. There are generally two ways of doing this. You can have the engine learn as it goes, or you can apply an algorithm which works for any environment (or use a combination, of course). The rules for submitting a bot for the mystery game are identical to those for chess. The only difference is that the class should be called `MysteryBot`. For the mystery game, we will implement a method (`get_state`) that outputs the state (or a description with everything that you need), as a Tensor.

## Learning across games

If you want the model to learn across games, you might want to save save some data to the disk, because your bot will be initialised and deleted before and after each game. To do this, you will need to create a directory-based bot (see the instructions above). Additionally, before your bot is deleted the `update` method is called. You have 2 minutes to do the processing you need to do when the `update` method is called. This time could be used to have the bot learn from it's past experiences.

## Getting started

To get started with this project clone this repository. Make sure to install the three dependencies `python-chess`, `tqdm`, and `torch`. To start building you own bot you can look at the example bots, stored in the `bots/` directory. One is a file-based bot, and one is a directory-based bot. Both implement a bot which makes random moves. Just copy one of these, give the file or directory a new name, and make some modifications. When you are happy with your changes you can run you new bot using the `play.py` file. Just modify the file by changing which engine is loaded (`load_engine("[your bot name here]")`), then go to the terminal and type:

```bash
python -m src.play
```

You can adjust the code in the `play.py` file to play against your bot, or to have your bot play against other bots. The chess board class is based on the `python-chess` library. You can take a closer look at [the docs](https://python-chess.readthedocs.io/en/latest/) for the details.

## Contacting us

Do you have notes, problems, or questions? Feel free to shoot us an email at <illuminatee@svcover.nl>.
