% Facts
student(john, cs).
student(sarah, math).
student(tom, physics).

teacher(alice, cs).
teacher(bob, math).
teacher(charlie, physics).

sub_code(cs, csci101).
sub_code(math, math101).
sub_code(physics, phys101).

% Predicate to check if a person is a student
is_student(Person) :-
    student(Person, _).

% Predicate to check if a person is a teacher
is_teacher(Person) :-
    teacher(Person, _).

% Predicate to find the subject associated with a student
student_subject(Student, Subject) :-
    student(Student, Subject).

% Predicate to find the subject associated with a teacher
teacher_subject(Teacher, Subject) :-
    teacher(Teacher, Subject).

% Predicate to find the subject code for a given subject
subject_code(Subject, Code) :-
    sub_code(Subject, Code).

% Predicate to find the teacher of a specific subject
teacher_of_subject(Subject, Teacher) :-
    teacher(Teacher, Subject).
