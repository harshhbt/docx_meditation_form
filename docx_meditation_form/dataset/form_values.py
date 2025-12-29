class FormValues:
    """
    Container for all per-user data required to populate the mediation DOCX form.

    A `FormValues` instance represents **one complete form submission** and is
    passed explicitly to dataset builders (e.g. `build_rows_dataset`) to render
    the document.

    Parameters
    ----------
    APPLICANT_NAME : str
        Full name of the applicant.
    APPLICANT_BRANCH_ADDRESS : str
        Registered / branch address of the applicant.
    APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS : str
        Correspondence address of the applicant.
    APPLICANT_PHONE : str
        Landline / phone number of the applicant.
    APPLICANT_MOBILE : str
        Mobile number of the applicant.
    APPLICANT_EMAIL_ID : str
        Email address of the applicant.

    DEFENDANT_NAME : str
        Full name of the defendant / opposite party.
    DEFENDANT_BRANCH_ADDRESS : str
        Registered / branch address of the defendant.
    DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS : str
        Correspondence address of the defendant.
    DEFENDANT_PHONE : str
        Landline / phone number of the defendant.
    DEFENDANT_MOBILE : str
        Mobile number of the defendant.
    DEFENDANT_EMAIL_ID : str
        Email address of the defendant.
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
