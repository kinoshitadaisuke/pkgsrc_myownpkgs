# $NetBSD$

BOOK_ONE=	UniversityPhysicsVol1-WEB.pdf
BOOK_TWO=	UniversityPhysicsVolume2-WEB_5eNhMSa.pdf
BOOK_THREE=	UniversityPhysicsVolume3-WEB.pdf
BOOK_FOUR=	College_Physics_2e-WEB_7Zesafu.pdf
BOOK_FIVE=	College_Physics_for_AP_Courses_2e-WEB_DkhNbxV.pdf

DISTNAME=	# empty
PKGNAME=	openstax-science-physics-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_ONE} ${BOOK_TWO} ${BOOK_THREE} ${BOOK_FOUR} ${BOOK_FIVE}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax Physics textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_ONE} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_TWO} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_THREE} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_FOUR} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_FIVE} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
