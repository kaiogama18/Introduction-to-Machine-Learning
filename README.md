# Introdução a Classificação | Machine Learning

Até agora vimos como a implementação do naive bayes funciona, ou seja, levando em consideração as informações do passado, ele da maiores preferência ao evento que aconteceu com mais frequência, portanto, se ele se deparar com um novo cliente que possui determinadas características e, baseado nas informações que ele já conhece, um mesmo cliente com as mesma características já comprou, provavelmente ele respondará que esse novo cliente comprará também.

Além do Multinomial, vimos também o AdaBoost que tenta se adaptar de acordo com o algoritmo para achar o melhor resultado, rodamos tanto o Multinomial quanto o AdaBoost e vimos que dependendo do conjunto de dados cada algoritmo obtem um resultado diferente. Também implementamos os 2 algoritmos no mesmo código para testá-los ao mesmo tempo, e então, aquele que retornava o melhor resultado, isto é, o maior resultado, escolhíamos como o algoritmo vencedor. Tendo o vencedor em mãos, fazíamos mais um teste que é justamente um teste do mundo real, em outras palavras, pegávamos novos elementos que ele nunca tinha visto antes, ou seja, nem no seu treino e nem no teste, então pedíamos para ele prevêr para nós, pois dessa forma podemos ter a certeza como será o seu comportamento, resultado dada uma situação do mundo real.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
