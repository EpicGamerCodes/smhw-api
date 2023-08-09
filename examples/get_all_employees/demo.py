import smhw_api as api

# Enter your account credentials
AUTH: str = ""
USER_ID: int = 0
SCHOOL_ID: int = 0


def main():
    server = api.Server(AUTH, USER_ID, SCHOOL_ID)
    school = server.get_current_school()  # get the student's school
    for (
        id
    ) in school.employee_ids:  # iterate through a list of the school's employee_ids
        try:
            employee = server.get_employee(
                id
            )  # get_user can also be used but it returns more data that is not needed for this function

        # Some employee's accounts that do not exist are also in this list
        # When the employee data can not be found, the `InvalidUser` exception is raised
        # The below code just skips accounts that do not exist.
        except api.exceptions.InvalidUser:
            continue

        # Print the employee id used to fetch the data
        # The employee's full name (this is auto generated by the dataclass)
        # When the employee's account was created
        print(f"{id} | {employee.full_name}, {employee.created_at}")


if __name__ == "__main__":
    main()