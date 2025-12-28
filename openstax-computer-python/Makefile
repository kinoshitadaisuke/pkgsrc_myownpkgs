# $NetBSD$

BOOK_ICS=	Introduction_To_Computer_Science_-_WEB.pdf
BOOK_PDS=	Principles-of-Data-Science-WEB.pdf
BOOK_IPP=	Introduction_to_Python_Programming_-_WEB.pdf

DISTNAME=	# empty
PKGNAME=	openstax-computer-python-1.0
CATEGORIES=	math science python
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${BOOK_ICS} ${BOOK_PDS} ${BOOK_IPP}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax computer science textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_ICS} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_PDS} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${BOOK_IPP} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
