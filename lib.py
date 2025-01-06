package library.model;

import java.time.LocalDate;
import java.util.*;

public class User {
    private int id;
    private String name;
    private String email;
    private UserType type;
    private List<Loan> activeLoans;
    private List<Reservation> reservations;

    public User(int id, String name, String email, UserType type) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.type = type;
        this.activeLoans = new ArrayList<>();
        this.reservations = new ArrayList<>();
    }

    // Getters e setters
}

public enum UserType {
    STUDENT, PROFESSOR, STAFF
}

public class Book {
    private int id;
    private String title;
    private String author;
    private String isbn;
    private BookCategory category;
    private int totalCopies;
    private int availableCopies;
    private List<BookCopy> copies;
    private List<Review> reviews;

    public Book(int id, String title, String author, String isbn, BookCategory category, int totalCopies) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.category = category;
        this.totalCopies = totalCopies;
        this.availableCopies = totalCopies;
        this.copies = new ArrayList<>();
        this.reviews = new ArrayList<>();
    }

    // Getters e setters
}

public class BookCopy {
    private int id;
    private Book book;
    private String location;
    private BookStatus status;
    private List<Loan> loanHistory;

    public BookCopy(int id, Book book, String location) {
        this.id = id;
        this.book = book;
        this.location = location;
        this.status = BookStatus.AVAILABLE;
        this.loanHistory = new ArrayList<>();
    }

    // Getters e setters
}

public enum BookStatus {
    AVAILABLE, LOANED, MAINTENANCE, LOST
}

public enum BookCategory {
    SCIENCE, TECHNOLOGY, ENGINEERING, MATHEMATICS, LITERATURE, HISTORY, ARTS
}

public class Loan {
    private int id;
    private User user;
    private BookCopy bookCopy;
    private LocalDate loanDate;
    private LocalDate dueDate;
    private LocalDate returnDate;
    private LoanStatus status;
    private List<Fine> fines;

    public Loan(int id, User user, BookCopy bookCopy) {
        this.id = id;
        this.user = user;
        this.bookCopy = bookCopy;
        this.loanDate = LocalDate.now();
        this.dueDate = loanDate.plusDays(14);
        this.status = LoanStatus.ACTIVE;
        this.fines = new ArrayList<>();
    }

    // Getters e setters
}

public enum LoanStatus {
    ACTIVE, OVERDUE, RETURNED, LOST
}

public class Fine {
    private int id;
    private Loan loan;
    private double amount;
    private String reason;
    private boolean paid;
    private LocalDate issueDate;
    private LocalDate paymentDate;

    public Fine(int id, Loan loan, double amount, String reason) {
        this.id = id;
        this.loan = loan;
        this.amount = amount;
        this.reason = reason;
        this.paid = false;
        this.issueDate = LocalDate.now();
    }

    // Getters e setters
}

public class Reservation {
    private int id;
    private User user;
    private Book book;
    private LocalDate reservationDate;
    private ReservationStatus status;

    public Reservation(int id, User user, Book book) {
        this.id = id;
        this.user = user;
        this.book = book;
        this.reservationDate = LocalDate.now();
        this.status = ReservationStatus.PENDING;
    }

    // Getters e setters
}

public enum ReservationStatus {
    PENDING, FULFILLED, CANCELLED, EXPIRED
}

public class Review {
    private int id;
    private User user;
    private Book book;
    private int rating;
    private String comment;
    private LocalDate reviewDate;

    public Review(int id, User user, Book book, int rating, String comment) {
        this.id = id;
        this.user = user;
        this.book = book;
        this.rating = rating;
        this.comment = comment;
        this.reviewDate = LocalDate.now();
    }

    // Getters e setters
}

// Service layer
package library.service;

public class LibraryService {
    private UserService userService;
    private BookService bookService;
    private LoanService loanService;
    private ReservationService reservationService;
    private FineService fineService;

    public LibraryService() {
        this.userService = new UserService();
        this.bookService = new BookService();
        this.loanService = new LoanService();
        this.reservationService = new ReservationService();
        this.fineService = new FineService();
    }

    // Metodi principali
}

public class UserService {
    private UserRepository userRepository;

    public User registerUser(String name, String email, UserType type) {
        // Implementazione
        return null;
    }

    public List<Loan> getUserLoans(int userId) {
        // Implementazione
        return null;
    }

    public List<Fine> getUserFines(int userId) {
        // Implementazione
        return null;
    }
}

public class BookService {
    private BookRepository bookRepository;

    public Book addBook(String title, String author, String isbn, BookCategory category, int copies) {
        // Implementazione
        return null;
    }

    public List<Book> searchBooks(String query) {
        // Implementazione
        return null;
    }

    public void updateBookAvailability(int bookId) {
        // Implementazione
    }
}

public class LoanService {
    private LoanRepository loanRepository;
    private BookService bookService;
    private FineService fineService;

    public Loan createLoan(int userId, int bookCopyId) {
        // Implementazione
        return null;
    }

    public void returnBook(int loanId) {
        // Implementazione
    }

    public void checkOverdueLoans() {
        // Implementazione
    }
}

public class ReservationService {
    private ReservationRepository reservationRepository;
    private BookService bookService;

    public Reservation createReservation(int userId, int bookId) {
        // Implementazione
        return null;
    }

    public void fulfillReservation(int reservationId) {
        // Implementazione
    }

    public void checkExpiredReservations() {
        // Implementazione
    }
}

public class FineService {
    private FineRepository fineRepository;

    public Fine createFine(int loanId, double amount, String reason) {
        // Implementazione
        return null;
    }

    public void payFine(int fineId) {
        // Implementazione
    }
}

// Repository layer
package library.repository;

public interface UserRepository {
    User save(User user);
    User findById(int id);
    List<User> findAll();
    void delete(int id);
}

public interface BookRepository {
    Book save(Book book);
    Book findById(int id);
    List<Book> findAll();
    List<Book> findByTitle(String title);
    void delete(int id);
}

public interface LoanRepository {
    Loan save(Loan loan);
    Loan findById(int id);
    List<Loan> findByUser(int userId);
    List<Loan> findOverdueLoans();
    void delete(int id);
}

public interface ReservationRepository {
    Reservation save(Reservation reservation);
    Reservation findById(int id);
    List<Reservation> findByUser(int userId);
    List<Reservation> findByBook(int bookId);
    void delete(int id);
}

public interface FineRepository {
    Fine save(Fine fine);
    Fine findById(int id);
    List<Fine> findByUser(int userId);
    void delete(int id);
}

// Utility classes
package library.util;

public class LibraryException extends RuntimeException {
    public LibraryException(String message) {
        super(message);
    }
}

public class ValidationUtils {
    public static void validateEmail(String email) {
        // Implementazione
    }

    public static void validateIsbn(String isbn) {
        // Implementazione
    }
}

public class DateUtils {
    public static boolean isOverdue(LocalDate dueDate) {
        return LocalDate.now().isAfter(dueDate);
    }

    public static int calculateDaysBetween(LocalDate start, LocalDate end) {
        // Implementazione
        return 0;
    }
}
