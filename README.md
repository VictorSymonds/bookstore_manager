# Bookstore Manager

This little project is a simulation of a virtual library that manages three different genres of books (books that I actually recommend a lot) and applies discounts and change of prices and automatic notification of recently added books

## Patrones de Diseño

Para este proyecto se utilizaron los patrones de diseño especificados:
    Factory Method (Creacional)
    Decorator (Estructural)
    Strategy (Comportamiento)
    Observer

## Factory Method
El problema que surgió es que se necesitaba una manera flexible de poder crear distintos tipos de libros según su género sin tener que acoplar directamente la lógica de creación a la clase principal y con este patrón logré delegar la creación de objetos a una subclase sin especificar su clase concreta. Por medio de la clase BookFactoy con el método create_book se retornan instancias especificas de libros según el género, eso significa que si quiero agregar nuevos géneros en el futuro no tendré que modificar la lógica principal.

## Decorator
El problema que surgió es que se necesitaba una manera de agregar funcionalidad adicional a un libro sin alterar la clase base y con este patrón logré añadir funcionalidades adicionales a un objeto dinamicamente y pues sin modificar su clase original. Por medio de la clase SignedBook prácticamente agarra un libro y agrega 5 dólares al precio y otra anotación en la descripción, así que puedo seguir utilizando el libro original pero con funcionalidad extendida.

## Strategy
El problema que surgió es que se necesitaba una manera de aplicar varios tipos de descuento a los libros sin tener que alterar la lógica interna de la clase Book y con este patrón logré encapsular los descuentos y hacerlos intercambiables sin tener que modificar la estructura de las clases que los usan. Por medio de StratDiscount y DiscountMember, cada libro puede tener su estrategia de descuento establecida dinamicamente.

## Observer
El problema que surgió es que se necesitaba una manera de notificar automáticamente a otras partes del sistema cuando un nuevo libro es añadido al sistema de gestión de libros y con este patrón logré que los objetos prácticamente se suscriban y reciban notificaciones cuando otro objeto cambia de estado. Por medio de BookManager se mantiene una lista de libros y notifica a BookObserver cada vez que se añade un nuevo libro.


## Diagrama UML
```mermaid
classDiagram
    class Book {
        +title
        +author
        +price
        +show_info()
        +set_strategy_discount()
        +get_price_with_discount()
    }

    class Scifi
    class NonFiction
    class Horror
    class SignedBook
    class BookFactory
    class StratDiscount {
        <<interface>>
        +apply_discount(price)
    }
    class DiscountMember {
        +apply_discount(price)
    }

    class BookManager {
        +register_observer()
        +add_book()
        +notify_observers()
    }

    class BookObserver {
        +update()
    }

    %% Relaciones
    Book <|-- Scifi
    Book <|-- NonFiction
    Book <|-- Horror
    Book <|-- SignedBook : <<Decorator>>
    StratDiscount <|.. DiscountMember : implementa
    Book o--> StratDiscount : utiliza
    SignedBook --> Book : envuelve
    BookFactory ..> Book : crea
    BookManager o--> Book : gestiona
    BookManager --> BookObserver : notifica