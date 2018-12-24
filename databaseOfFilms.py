from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, ItemTitle, engine


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# User functions
def create_user(name, email, picture):
    new_user = User(
        name=name,
        email=email,
        picture=picture
        )
    session.add(new_user)
    session.commit()
    return new_user.id


def get_user(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# def del_user(user_id):
#     user = session.query(User).filter_by(id=user_id).one()
#     session.delete(user)
#     session.commit()


# Category functions
def create_category(name):
    new_category = Category(name=name)
    session.add(new_category)
    session.commit()
    return new_category.id


def get_cat_id(name):
    cat = session.query(Category).filter_by(name=name).one()
    return cat.id


def get_items_in_category(category_name):
    items_list = session.query(ItemTitle).join(ItemTitle.category).filter_by(name=category_name)
    return items_list


# ItemTitle functions
def create_item(name, description, category_id, user_id):
    new_film = ItemTitle(
        name=name,
        description=description,
        category_id=category_id,
        user_id=user_id
        )
    session.add(new_film)
    session.commit()
    return new_film.id


# set up functions:

def add_users():
    user_list = [
        ['', '', '']
    ]

    for user in user_list:
        create_user(user[0], user[1], user[2])


def fill_categories():
    cat_list = [
        'Action',
        'Adventure',
        'Comedy',
        'Crime',
        'Horror',
        'Sport',
        'Family'
    ]

    for cat in cat_list:
        create_category(cat)


def fill_items():

    films_col = [
        (
            'Aquaman ',
            'Arthur Curry learns that he is the heir to the underwater kingdom of Atlantis, and must step forward to lead his people and be a hero to the world.',
            'Action'
            ),
        (
            'Spider-Man: Into the Spider-Verse',
            'Miles Morales becomes the Spider-Man of his reality and crosses paths with his counterparts from other dimensions to stop a threat to all reality.',
            'Action'
            ),
        (
            'Mission: Impossible - Fallout',
            'Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.',
            'Action'
            ),
        (
            'Gladiator',
            'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery..',
            'Adventure'
            ),
        (
            'Inception',
            'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO..',
            'Adventure'
            ),
        (
            'Home Alone',
            'An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.',
            'Comedy'
            ),
        (
            'Office Space',
            'Three company workers who hate their jobs decide to rebel against their greedy boss.',
            'Comedy'
            ),
        (
            'The Dark Knight',
            'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham. The Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
            'Crime'
            ),
        (
            'Kidnap',
            'A mother stops at nothing to recover her kidnapped son.',
            'Crime'
            ),
        (
            'A Quiet Place',
            'In a post-apocalyptic world, a family is forced to live in silence while hiding from monsters with ultra-sensitive hearing..',
            'Horror'
            ),
        (
            'Hereditary ',
            'After the family matriarch passes away, a grieving family is haunted by tragic and disturbing occurrences, and begin to unravel dark secrets.',
            'Horror'
            ),
        (
            'Creed ',
            'The former World Heavyweight Champion Rocky Balboa serves as a trainer and mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed.',
            'Sport'
            ),
        (
            'The Fate of the Furiou',
            'When a mysterious woman seduces Dom into the world of terrorism and a betrayal of those closest to him, the crew face trials that will test them as never before.',
            'Sport'
            ),
        (
            'Hachi: A Dogs Tale',
            'A college professors bond with the abandoned dog he takes into his home.',
            'Family'
            ),
        (
            'Nanny McPhee',
            'A governess uses magic to rein in the behavior of seven neer-do-well children in her charge.',
            'Family'
            )
    ]
    print "added films!"

    for col in films_col:
        create_item(
            col[0],
            col[1],
            get_cat_id(col[2]),
            1
            )


if __name__ == '__main__':
    add_users()
    fill_categories()
    fill_items()
