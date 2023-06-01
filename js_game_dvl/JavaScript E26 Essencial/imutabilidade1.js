const user = {
    name: 'Bárbara',
    lastName: 'Arruda'
};

function getUserWithFullName(user) {
    return {
        ...user,
        fullName: '${user.name} ${user.lastName}' //serve como concatenação
    }
}

const userWithFullName = getUserWithFullName(user);

console.log(userWithFullName, user);
