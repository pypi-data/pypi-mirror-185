class Operations(object):

    # These are the banking integrations
    # Each with a unique ID
    GLOBAL = 0
    COOP = GLOBAL + 1
    EQUITY = COOP + 1
    NCBA = EQUITY + 1
    DAPI = NCBA + 1
    MONO = DAPI + 1
    PLAID = MONO + 1
    STITCH = PLAID + 1
    DTB = STITCH + 1
    UBA = DTB + 1
    KCB = UBA + 1
    SCB = KCB + 1
    SAFCOM = SCB + 1
    FAULU = SAFCOM + 1
    CONSOLIDATED = FAULU + 1
    STANBIC = CONSOLIDATED + 1
    FAMILY=STANBIC + 1
    NCBA_LOOP=FAMILY + 1

    # These are the operations to be performed in Banking Identity
    # Each with a unique incremental ID

    # Returns Sample Data
    OPERATIONS = -2
    SAMPLE_DATA = OPERATIONS + 1
    BANKS = SAMPLE_DATA + 1
    BALANCE = BANKS + 1
    MINI_STATEMENT = BALANCE + 1
    FULL_STATEMENT = MINI_STATEMENT + 1
    ACCOUNT_VALIDATION = FULL_STATEMENT + 1
    ACCOUNT_TRANSACTIONS = ACCOUNT_VALIDATION + 1
    IFT = ACCOUNT_TRANSACTIONS + 1
    TRANSACTION_STATUS = IFT + 1
    MOBILE_WALLET = TRANSACTION_STATUS + 1
    PESALINK_TO_BANK = MOBILE_WALLET + 1
    PESALINK_TO_MOBILE = PESALINK_TO_BANK + 1
    RTGS = PESALINK_TO_MOBILE + 1
    SWIFT = RTGS + 1
    EFT = SWIFT + 1
    OMN = EFT + 1
    INITIATE_PAYMENT = OMN + 1
    FOREX_RATE = INITIATE_PAYMENT + 1
    COUNTRIES = FOREX_RATE + 1
    STK_PUSH = COUNTRIES + 1
    BANKS_BY_CODE = STK_PUSH + 1
    BANKS_BY_ID = BANKS_BY_CODE + 1
    PDF_TO_JSON = BANKS_BY_ID + 1
    GET_JSON_PDF = PDF_TO_JSON + 1
    IPN_REGISTER = GET_JSON_PDF + 1
    IPN_GET = IPN_REGISTER + 1
    IPN_UPDATE = IPN_GET + 1
    IPN_DELETE = IPN_UPDATE + 1
    IPN_GENERATE_CLIENT_SECRET = IPN_DELETE + 1
    JOBS_ACCOUNT_BALANCES = IPN_GENERATE_CLIENT_SECRET + 1
    JOBS_ACCOUNT_STATEMENT = JOBS_ACCOUNT_BALANCES + 1

    # All end points are placed in the BANKS_CONF
    # This is to allow easy standardization of the base url, endpoint and operations
    # When calling the APIs, in this case this is done in the resource class read function
    BANKS_CONF = {
        GLOBAL: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "read": {
                "endpoint": f"api/banks",
                "operations": {
                    OPERATIONS: ("operations", "GET"),
                    SAMPLE_DATA: ("sample_payload", "POST"),
                    BANKS: ("banks", "GET"),
                    BANKS_BY_CODE: ("banks/by_code", "GET"),
                    BANKS_BY_ID: ("banks/by_id", "GET"),
                    COUNTRIES: ("countries", "GET"),
                    IPN_REGISTER: ("ipn/register", "POST"),
                    IPN_GET: ("ipn/get", "POST"),
                    IPN_UPDATE: ("ipn/update", "POST"),
                    IPN_DELETE: ("ipn/delete", "POST"),
                    IPN_GENERATE_CLIENT_SECRET: ("ipn/generate_client_secret", "POST"),
                    JOBS_ACCOUNT_BALANCES: ("jobs/account_balances", "POST"),
                    JOBS_ACCOUNT_STATEMENT: ("jobs/account_statement", "POST"),
                }
            }

        },
        UBA: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{UBA}",
                "operations": {
                    BALANCE: ("get_balance", "POST"),
                    FULL_STATEMENT: ("get_full_statement", "POST"),
                }
            },
            "payment": {
                "endpoint": f"api/banks/payment/{UBA}",
                "operations": {
                    IFT: ("ift", "POST"),
                }
            }

        },
        DTB: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{DTB}",
                "operations": {
                    ACCOUNT_VALIDATION: ("get_validation", "POST"),
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {
                "endpoint": f"api/banks/payment/{DTB}",
                "operations": {
                    IFT: ("ift", "POST"),
                    MOBILE_WALLET: ("mobile_wallet", "POST"),
                    TRANSACTION_STATUS: ("get_transaction_status", "POST"),
                    STK_PUSH: ("c2b_stk_push", "POST"),
                }
            }

        },
        EQUITY: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{EQUITY}",
                "operations": {
                    BALANCE: ("get_balance", "POST"),
                    MINI_STATEMENT: ("get_mini_statement", "POST"),
                    ACCOUNT_VALIDATION: ("get_validation", "POST"),
                    FULL_STATEMENT: ("get_full_statement", "POST"),
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                    FOREX_RATE: ("forex_rate", "POST")
                }
            },
            "payment": {
                "endpoint": f"api/banks/payment/{EQUITY}",
                "operations": {
                    IFT: ("ift", "POST"),
                    MOBILE_WALLET: ("mobile_wallet", "POST"),
                    RTGS: ("rtgs", "POST"),
                    SWIFT: ("swift", "POST"),
                    EFT: ("eft", "POST"),
                    PESALINK_TO_BANK: ("pesalink/bank", "POST"),
                    PESALINK_TO_MOBILE: ("pesalink/mobile", "POST"),
                    TRANSACTION_STATUS: ("get_transaction_status", "POST"),
                }
            }

        },
        COOP: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{COOP}",
                "operations": {
                    BALANCE: ("get_balance", "POST"),
                    MINI_STATEMENT: ("get_mini_statement", "POST"),
                    ACCOUNT_VALIDATION: ("get_validation", "POST"),
                    FULL_STATEMENT: ("get_full_statement", "POST"),
                    ACCOUNT_TRANSACTIONS: ("get_transactions", "POST"),
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {
                "endpoint": f"api/banks/payment/{COOP}",
                "operations": {
                    IFT: ("ift", "POST"),
                    MOBILE_WALLET: ("mobile_wallet", "POST"),
                    PESALINK_TO_BANK: ("pesalink/bank", "POST"),
                    PESALINK_TO_MOBILE: ("pesalink/mobile", "POST"),
                    TRANSACTION_STATUS: ("get_transaction_status", "POST"),
                }
            }

        },
        NCBA: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{NCBA}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {
                "endpoint": f"api/banks/payment/{NCBA}",
                "operations": {
                    IFT: ("ift", "POST"),
                    MOBILE_WALLET: ("mobile_wallet", "POST"),
                    RTGS: ("rtgs", "POST"),
                    EFT: ("eft", "POST"),
                    PESALINK_TO_BANK: ("pesalink/bank", "POST"),
                    TRANSACTION_STATUS: ("get_transaction_status", "POST"),
                }
            }
        },
        SAFCOM: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{SAFCOM}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
        SCB: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{SCB}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
        KCB: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{KCB}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
        FAULU: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{FAULU}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
        CONSOLIDATED: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{CONSOLIDATED}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
        STANBIC: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{STANBIC}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
        FAMILY: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{FAMILY}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
        NCBA_LOOP: {
            "url": "https://dev.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/banks/accounts/{NCBA_LOOP}",
                "operations": {
                    PDF_TO_JSON: ("pdf_to_json", "POST"),
                    GET_JSON_PDF: ("uploaded_pdf_json", "POST"),
                }
            },
            "payment": {}
        },
    }

    THIRD_PARTY_BANKING = {
        DAPI: {
            "url": "https://dev.3p.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/v1/Dapi",
                "operations": {
                    BALANCE:  ("get_balance", "POST"),
                    ACCOUNT_TRANSACTIONS: ("get_transactions", "POST")
                }                
            },
            "payment": {
                "endpoint": f"api/v1/Dapi",
                "operations": {
                    INITIATE_PAYMENT: ("initiate_payment", "POST"),
                }
            }
        },
        MONO: {
            "url": "https://dev.3p.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/v1/Mono",
                "operations": {
                    BALANCE:  ("get_balance", "POST"),
                    ACCOUNT_TRANSACTIONS: ("get_transactions", "POST")
                }                
            },
            "payment": {
                "endpoint": f"api/v1/Mono",
                "operations": {
                    INITIATE_PAYMENT: ("initiate_payment", "POST"),
                }
            }
        },
        PLAID: {
            "url": "https://dev.3p.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/v1/Plaid",
                "operations": {
                    BALANCE:  ("get_balance", "POST"),
                    ACCOUNT_TRANSACTIONS: ("get_transactions", "POST")
                }                
            },
            "payment": {
                "endpoint": f"api/v1/Plaid",
                "operations": {
                    INITIATE_PAYMENT: ("initiate_payment", "POST"),
                }
            }
        },
        STITCH: {
            "url": "https://dev.3p.bankingservices.nashglobal.co",
            "accounts": {
                "endpoint": f"api/v1/Stitch",
                "operations": {
                    BALANCE:  ("get_balance", "POST"),
                    ACCOUNT_TRANSACTIONS: ("get_transactions", "POST")
                }                
            },
            "payment": {
                "endpoint": f"api/v1/Stitch",
                "operations": {
                    INITIATE_PAYMENT: ("initiate_payment", "POST"),
                }
            }
        },
    }
