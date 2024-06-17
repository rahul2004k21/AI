food(chicken_breast, 165, 31, 3.6, 0).
food(broccoli, 55, 3.7, 0.6, 11.2).
food(rice, 130, 2.4, 0.3, 28.7).

vegetarian(broccoli).
vegetarian(rice).

gluten_free(chicken_breast).
gluten_free(broccoli).
gluten_free(rice).

suitable_for_vegetarian(Food) :- vegetarian(Food).
suitable_for_gluten_free(Food) :- gluten_free(Food).


