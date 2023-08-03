# $NetBSD: Makefile,v 1.17 2022/01/05 15:41:12 wiz Exp $

DISTNAME=	qrcode-7.4.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	graphics python
MASTER_SITES=	${MASTER_SITE_PYPI:=q/qrcode/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.python.org/pypi/qrcode
COMMENT=	Python QR Code image generator
LICENSE=	modified-bsd

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=48:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-lxml>=0:../../textproc/py-lxml
DEPENDS+=	${PYPKGPREFIX}-six>=0:../../lang/py-six
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-pypng>=0.20220715.0:../../pkgsrc_myownpkgs/py-pypng

PYTHON_VERSIONS_INCOMPATIBLE=	27

PYTHON_VERSIONED_DEPENDENCIES=	Pillow

USE_PKG_RESOURCES=	yes

USE_LANGUAGES=	# none

REPLACE_PYTHON+=	qrcode/console_scripts.py

SUBST_CLASSES+=			pkgmandir
SUBST_FILES.pkgmandir=		setup.py
SUBST_MESSAGE.pkgmandir=	Fixing PKGMANDIR path.
SUBST_SED.pkgmandir=		-e "s|share/man|${PKGMANDIR}|1"
SUBST_STAGE.pkgmandir=		pre-configure

post-install:
	${MV} ${DESTDIR}${PREFIX}/bin/qr \
		${DESTDIR}${PREFIX}/bin/qr-${PYVERSSUFFIX} || ${TRUE}
	${MV} ${DESTDIR}${PREFIX}/${PKGMANDIR}/man1/qr.1 \
		${DESTDIR}${PREFIX}/${PKGMANDIR}/man1/qr-${PYVERSSUFFIX}.1 || ${TRUE}

.include "../../lang/python/application.mk"
.include "../../lang/python/egg.mk"
.include "../../lang/python/versioned_dependencies.mk"
.include "../../mk/bsd.pkg.mk"
