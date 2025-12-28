# $NetBSD$

BOOK_IS=	IntroductoryStatistics-OP_i6tAI7e.pdf
BOOK_IS2E=	Introductory_Statistics_2e_-_WEB.pdf
BOOK_IBS2E=	Introductory_Business_Statistics_2e_-_WEB.pdf
BOOK_HSS=	Statistics-WEB.pdf

DISTNAME=	# empty
PKGNAME=	openstax-math-statistics-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_IS} ${BOOK_IS2E} ${BOOK_IBS2E} ${BOOK_HSS}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax Introductory Statistics textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_IS} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_IS2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_IBS2E} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_HSS} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
