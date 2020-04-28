# photoacoustic-signal-scanner
A little program to make a photoacustic scan and graphics.

## Getting Started

### How Does It Work?
This project workes in a photoacoustic spectroscopy experiment. Brieafly, it takes the x and y values from a [lock-in amplifier](https://www.thinksrs.com/downloads/pdfs/manuals/SR830m.pdf), and they are saved in a csv file. These values can be used to calculate the value of R and &theta;. Finally the program plots the R-values which is the amplitude of the filtered signal.

The lock-in amplifier reads the values and send to the program. The parameters are taken through GPIB cable connected on the lock-in amplifier. Through PyVisa, which intermediates the communication between the computer and the lockin, python takes the values. 

### Usage
This program workes in a tipical photoacoustic gase experiment. Just download the file and use, but be carefull about the libraries which are necessary. This program worked in a tipical You can see a list of them below.

### Dependencies
- [NumPy](https://numpy.org/)
- [PyVisa](https://pyvisa.readthedocs.io/en/latest/)
- [SciPy](https://www.scipy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Drawnow](https://github.com/stsievert/python-drawnow)

## Acknowledgment
- State University of Northern Fluminense Darcy Ribeiro ([UENF](http://uenf.br/))
- Graduate Program in Natural Sciences ([PGCN](http://uenf.br/posgraduacao/ciencias-naturais/))
- UENF Gas Photoacoustic Study Group

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details