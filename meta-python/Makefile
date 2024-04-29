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

# devel
DEPENDS+=	${PYPKGPREFIX}-gitpython>=0:../../devel/py-gitpython
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-ipython>=0:../../devel/py-ipython
DEPENDS+=	${PYPKGPREFIX}-pip>=0:../../devel/py-pip
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test

# graphics
DEPENDS+=	${PYPKGPREFIX}-exifread>=0:../../graphics/py-exifread
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib

# math
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-image>=0:../../math/py-scikit-image
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-sympy>=0:../../math/py-sympy
DEPENDS+=	${PYPKGPREFIX}-uncertainties>=0:../../math/py-uncertainties

# www
DEPENDS+=	${PYPKGPREFIX}-notebook>=0:../../www/py-notebook
DEPENDS+=	${PYPKGPREFIX}-jupyterlab>=0:../../www/py-jupyterlab

# pkgsrc_myownpkgs
DEPENDS+=	${PYPKGPREFIX}-qrcode>=0:../../pkgsrc_myownpkgs/py-qrcode
DEPENDS+=	${PYPKGPREFIX}-geopandas>=0:../../pkgsrc_myownpkgs/py-geopandas

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
