# $NetBSD$

VOL_ONE=	Calculus_Volume_1_-_WEB_68M1Z5W.pdf
VOL_TWO=	CalculusVolume2-OP.pdf
VOL_THREE=	CalculusVolume3-OP_mktoy8b.pdf

DISTNAME=	# empty
PKGNAME=	openstax-math-calculus-1.0
CATEGORIES=	math science
MASTER_SITES=	https://assets.openstax.org/oscms-prodcms/media/documents/
DISTFILES=	${VOL_ONE} ${VOL_TWO} ${VOL_THREE}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://assets.openstax.org/oscms-prodcms/media/documents/
COMMENT=	OpenStax Calculus textbooks
LICENSE=	cc-by-v4.0

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none

NO_BUILD=	yes

do-install:
	${MKDIR} -p ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${VOL_ONE} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${VOL_TWO} ${DESTDIR}${PREFIX}/share/doc/openstax
	${INSTALL_DATA} ${WRKSRC}/${VOL_THREE} ${DESTDIR}${PREFIX}/share/doc/openstax

.include "../../mk/bsd.pkg.mk"
