# Owler

Owler is a library to help manage [Project Euler](https://projecteuler.net) solving programming files, potentially in
multiple languages. You know, no easier way to play around with Rust/Octave/`$LANGUAGE` than trying some Project Euler
problems in it!


## Usage

Only just begun, nothing usable here yet.

First, you will need to install `tesseract`. Please see [here](https://github.com/tesseract-ocr/tesseract/wiki) for
installation information. Any language with arabic digits should do as language base.


## Features

 - create problem solving file(s) in a language of your choice, or multiple languages
 - provide the problem description as comment string in the files
 - load additional data such as images in the problem directory
 - submit your solution to [projecteuler](https://projecteuler.net) or just print the result
 - pre-fetch all problem data to be network independent afterwards
 - usage: command line flags or interactive mode
 - available for installation with `pip`


## Challenges

Project Euler uses a Captcha to prevent people from spamming the server with possible solutions. For now I'll use the
lazy solution of throwing tesseract at the captcha. Maybe I'll follow up with a neural network solution afterwards, to
remove the large and hard external dependency on tesseract.
This script will enforce its own rate limiting to avoid easy spamming of the ProjectEuler site.


## Contributing

Contributions are welcome. Shoot me an issue, PR or mail if you have any questions or ideas here! Look
[here](CONTRIBUTING.md) for more detailed information regarding contributions, and please also look at this project's
[Code of Conduct](CODE_OF_CONDUCT.md).
