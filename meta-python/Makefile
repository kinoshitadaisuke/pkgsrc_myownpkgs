# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-python-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for astronomy
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# graphics
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib

# math
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-image>=0:../../math/py-scikit-image
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-uncertainties>=0:../../math/py-uncertainties

# pkgsrc_myownpkgs
DEPENDS+=	${PYPKGPREFIX}-qrcode>=0:../../pkgsrc_myownpkgs/py-qrcode

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
