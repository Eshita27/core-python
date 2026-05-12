def test_user(user):
    print(f"\nTesting with user: {user['username']}")
    assert user["username"] == "Eshita"