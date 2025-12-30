class FormValues:
    """
    Container for all per-user data required to populate the mediation DOCX form.

    A `FormValues` instance represents **one complete form submission** and is
    passed explicitly to dataset builders (e.g. `build_rows_dataset`) to render
    the document.

    :param APPLICANT_NAME: Full name of the applicant.
    :param APPLICANT_BRANCH_ADDRESS: Registered / branch address of the applicant.
    :param APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS: Correspondence address of the applicant.
    :param APPLICANT_PHONE: Landline / phone number of the applicant.
    :param APPLICANT_MOBILE: Mobile number of the applicant.
    :param APPLICANT_EMAIL_ID: Email address of the applicant.

    :param DEFENDANT_NAME: Full name of the defendant / opposite party.
    :param DEFENDANT_BRANCH_ADDRESS: Registered / branch address of the defendant.
    :param DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS: Correspondence address of the defendant.
    :param DEFENDANT_PHONE: Landline / phone number of the defendant.
    :param DEFENDANT_MOBILE: Mobile number of the defendant.
    :param DEFENDANT_EMAIL_ID: Email address of the defendant.
    """

    def __init__(
        self,
        *,
        # Applicant
        APPLICANT_NAME="",
        APPLICANT_BRANCH_ADDRESS="",
        APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS="",
        APPLICANT_PHONE="",
        APPLICANT_MOBILE="",
        APPLICANT_EMAIL_ID="",
        # Defendant
        DEFENDANT_NAME="",
        DEFENDANT_BRANCH_ADDRESS="",
        DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS="",
        DEFENDANT_PHONE="",
        DEFENDANT_MOBILE="",
        DEFENDANT_EMAIL_ID="",
    ):
        placeholder = "________________"
        # applicant
        self.APPLICANT_NAME = APPLICANT_NAME

        self.APPLICANT_BRANCH_ADDRESS = (
            APPLICANT_BRANCH_ADDRESS
            if APPLICANT_BRANCH_ADDRESS and APPLICANT_BRANCH_ADDRESS != ""
            else placeholder
        )
        self.APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS = (
            APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS
            if APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS
            and APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS != ""
            else placeholder
        )

        self.APPLICANT_PHONE = APPLICANT_PHONE
        self.APPLICANT_MOBILE = APPLICANT_MOBILE
        self.APPLICANT_EMAIL_ID = APPLICANT_EMAIL_ID

        # defendant
        self.DEFENDANT_NAME = DEFENDANT_NAME

        self.DEFENDANT_BRANCH_ADDRESS = (
            DEFENDANT_BRANCH_ADDRESS
            if DEFENDANT_BRANCH_ADDRESS and DEFENDANT_BRANCH_ADDRESS != ""
            else placeholder
        )
        self.DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS = (
            DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS
            if DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS
            and DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS != ""
            else placeholder
        )

        self.DEFENDANT_PHONE = DEFENDANT_PHONE
        self.DEFENDANT_MOBILE = DEFENDANT_MOBILE
        self.DEFENDANT_EMAIL_ID = DEFENDANT_EMAIL_ID
