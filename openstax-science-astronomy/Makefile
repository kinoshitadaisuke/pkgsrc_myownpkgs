# $NetBSD$

DISTNAME=	Astronomy-2e-WEB_6qnoaIc
PKGNAME=	openstax-science-astronomy
CATEGORIES=	math
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
EXTRACT_SUFX=	.pdf

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	Textbook OpenStax Astronomy 2e
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${DISTNAME}${EXTRACT_SUFX} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
