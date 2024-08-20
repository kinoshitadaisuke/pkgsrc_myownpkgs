# $NetBSD$

BOOK_ONE=	Calculus_Volume_1_-_WEB_68M1Z5W.pdf
BOOK_TWO=	Calculus_Volume_2_-_WEB.pdf
BOOK_THREE=	Calculus_Volume_3_-_WEB.pdf
BOOK_FOUR=	Precalculus_2e-WEB.pdf

DISTNAME=	# empty
PKGNAME=	openstax-math-calculus-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_ONE} ${BOOK_TWO} ${BOOK_THREE} ${BOOK_FOUR}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax Calculus textbooks
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

.include "../../mk/bsd.pkg.mk"
